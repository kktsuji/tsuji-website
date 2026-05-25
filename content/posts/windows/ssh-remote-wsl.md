---
title: "SSH into WSL on a Remote Windows Machine"
description: ""
date: 2026-05-23T16:30:00+09:00
lastmod:
draft: false
---

To SSH from a client into WSL on a remote Windows machine, use one of the following approaches:

1. SSH Jumphost (recommended)
2. Windows port forwarding feature

## Prerequisites

You should already be able to SSH into the remote Windows machine as described in [this article](https://tsuji.tech/ssh-remote-windows/). If you have not set this up yet, please establish SSH access to the remote Windows machine first by following that guide.

## Install the OpenSSH Server on the Remote WSL

Regardless of which approach you choose, you need to install the OpenSSH server on the remote Windows's WSL side and have it listen on a port that does not collide with the Windows side.

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install openssh-server -y
```

Change the port configuration to a port that does not collide with the Windows side (22), e.g. `Port 22222`:

```bash
sudo vim /etc/ssh/sshd_config
```

Restart the SSH server:

```bash
sudo service ssh restart
```

Verify that sshd is listening on 22222:

```bash
ss -tlnp | grep 22222

# Example output
# LISTEN 0      128           0.0.0.0:22222      0.0.0.0:*
# LISTEN 0      128              [::]:22222         [::]:*
```

Once this is configured, confirm that you can SSH from the remote Windows machine into WSL.

```powershell
# WSL password required
ssh -p 22222 wsluser@localhost
```

## Windows Configuration (Using a Jumphost)

This approach uses the SSH server on the remote Windows machine as a jumphost, and connects from the client to the remote WSL via SSH's ProxyJump feature.

It is recommended over the port-forwarding approach because the configuration is simpler.

### Prerequisites of Mirrored Mode

To use mirrored mode, the following are required:

- Host OS: Windows 11 22H2 or later
- WSL version: WSL v2.0.4 or later `(check with wsl --version)`

### WSL Configuration on the Host

Add the following to `C:\Users\<username>\.wslconfig` on the host:

```ini
[wsl2]
networkingMode=mirrored
vmIdleTimeout=-1

[experimental]
hostAddressLoopback=true
```

- networkingMode=mirrored: WSL is connected directly to the same network as the host, so the WSL IP address becomes the same as the host's. This allows the client to SSH into WSL directly.
- hostAddressLoopback=true: An experimental setting that requires mirrored mode. It allows connections between the container (WSL) and the host using the IP address assigned to the host. This makes it possible to SSH into WSL using the host's IP address. Only the IPv4 address assigned to the host is supported; IPv6 is not.
- vmIdleTimeout=-1: Disables the WSL idle timeout. With this, WSL will not automatically stop even after a period of inactivity.

After saving, restart WSL on the host.

```powershell
wsl --shutdown
```

Additionally, configure WSL to start automatically when Windows boots.

- Open Task Scheduler with `Win + R` + `taskschd.msc`
- Click "Create Task" in the right pane
- "General" tab:
  - Name: e.g. "Start WSL on Login"
  - Security options: select "Run only when user is logged on"
  - Check "Run with highest privileges"
- "Triggers" tab:
  - Click "New"
  - Begin the task: "At log on"
  - Settings: check "Specific user" and select the user
  - Delay task for: about 30 seconds to 1 minute (for stability)
  - Enabled: checked
- "Actions" tab:
  - Click "New"
  - Action: "Start a program"
  - Program/script: `wsl.exe`
  - Add arguments: `-d Ubuntu --exec dbus-launch true`
  - Start in: leave blank

With this, the command `wsl -d Ubuntu --exec dbus-launch true` will run at Windows startup and WSL will start automatically.

### WSL Configuration

Add the following to `/etc/wsl.conf`. This makes sshd start automatically when WSL boots.

```ini
[boot]
systemd=true
```

Then enable the SSH server to start automatically with the following command.

```bash
sudo systemctl enable ssh
```

Restart WSL on the host.

```powershell
wsl --shutdown
```

With this set of configurations:

- WSL starts up reliably:
  - WSL starts automatically when Windows boots
  - systemd is enabled inside WSL and the SSH server starts automatically
  - WSL does not stop automatically after a period of inactivity
- You can SSH stably from the client to WSL on the host Windows:
  - The WSL IP and the host Windows IP match (preventing IP changes on each WSL startup)
  - You can specify the WSL IP as 127.0.0.1 when using ProxyJump

### How to Configure ProxyJump

Add the following to the client's `~/.ssh/config`.

Note: specify `127.0.0.1` — **not** `localhost` — for the HostName of remote-wsl. If you specify `localhost`, depending on the environment it may connect over IPv6 and fail. Specifying `127.0.0.1` ensures the connection is made explicitly over IPv4.

```bash
Host remote-win
  HostName <hostname>  # or <hostname>.local or <ip-address>
  User windowsuser

Host remote-wsl
  HostName 127.0.0.1 # explicitly specify IPv4
  User wsluser
  Port 22222
  ProxyJump remote-win
```

This lets you connect easily from the client with the following command.

```bash
ssh remote-wsl
```

### (Optional) Updating the WSL IP Address When Not Using Mirrored Mode

If you do not use mirrored mode and WSL has a different IP address from the host, some extra care is needed.

WSL runs on a virtual NIC and its IP changes every time it starts, so the `HostName` in the client's `~/.ssh/config` also needs to be updated.

It is convenient to create an update script on the client side.

First, check the path of your profile.

```powershell
$PROFILE
```

It typically looks something like `C:\Users\kouki\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`.

If the file does not exist, create it with the following command.

```powershell
if (-not (Test-Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}
```

Next, open the profile in VSCode or similar,

```powershell
code $PROFILE
```

and add the following function to the end of the file.

```powershell
function Update-WslIp {
    [CmdletBinding()]
    param(
        [string]$JumpHost = 'winusername@hostname',  # Jumphost username and hostname
        [string]$ConfigPath = "$HOME\.ssh\config",
        [string]$TargetHost = 'remote-wsl'
    )

    Write-Host "Fetching WSL IP via $JumpHost..." -ForegroundColor Cyan
    $wslIp = (ssh $JumpHost 'wsl hostname -I' 2>$null).Trim().Split(' ')[0]

    if (-not $wslIp) {
        Write-Error "Failed to get WSL IP address"
        return
    }

    if (-not (Test-Path $ConfigPath)) {
        Write-Error "$ConfigPath not found"
        return
    }

    # Get current IP (early return if no change is needed)
    $content = Get-Content $ConfigPath -Raw
    $pattern = "(?ms)(Host\s+$TargetHost\s*\r?\n(?:[^\r\n]*\r?\n)*?\s*HostName\s+)(\S+)"
    $currentMatch = [regex]::Match($content, $pattern)
    $currentIp = if ($currentMatch.Success) { $currentMatch.Groups[2].Value } else { $null }

    if ($currentIp -eq $wslIp) {
        Write-Host "IP is already up to date: $wslIp" -ForegroundColor Green
        return
    }

    # Back up and replace
    Copy-Item $ConfigPath "$ConfigPath.bak" -Force
    $updated = $content -replace $pattern, "`${1}$wslIp"
    Set-Content -Path $ConfigPath -Value $updated -NoNewline

    Write-Host "Updated: $currentIp -> $wslIp" -ForegroundColor Green
}

# Short alias (optional)
Set-Alias uwsl Update-WslIp
```

Restart PowerShell or reload the profile.

```powershell
. $PROFILE
```

You can then use it with the following commands.

```powershell
# Alias
uwsl

# Full command
Update-WslIp -JumpHost 'windowsuser@hostname' -TargetHost 'remote-wsl'
```

## Windows Configuration (Using Port Forwarding)

If you are in an environment where using a Jumphost is not possible, you can instead use the Windows portproxy feature to forward connections to a specific port on the remote Windows machine (e.g. 22222) to the WSL SSH server.

The following commands are run in an Administrator PowerShell on the remote Windows machine.

### Configuring the portproxy Listening Port

Get the IP address of WSL and configure port forwarding via Windows portproxy.

WSL may report two or more IP addresses (e.g. IPv4 and IPv6, Docker), so take the first one (IPv4).

```powershell
# Get the WSL IP address (IPv4)
$wslIp = (wsl hostname -I).Trim().Split(' ')[0]

# Configure port forwarding with Windows portproxy
netsh interface portproxy add v4tov4 listenport=22222 listenaddress=0.0.0.0 connectport=22222 connectaddress=$wslIp

# Verify
# It is OK if it shows something like: Listen on ipv4: 0.0.0.0:22222 → Connect to ipv4: 172.x.x.x:22222
netsh interface portproxy show v4tov4
```

### Allow Port 22222 in the Firewall

Opening this port in Windows Defender Firewall allows external clients to connect to the WSL SSH server.

```powershell
New-NetFirewallRule -DisplayName "WSL SSH" -Direction Inbound -LocalPort 22222 -Protocol TCP -Action Allow
```

### Connecting via SSH from the Client to the Remote WSL

Verify the connection as follows.

Note: explicitly specify the `-4` option to connect over IPv4. Without it, IPv6 may be used depending on the environment, and the connection may fail.

```powershell
ssh -4 -p 22222 wsluser@<hostname>
```

If the connection succeeds, you are now SSH'd into WSL on the remote Windows machine.

If you want to connect without a password, generate an SSH key and place the public key on the remote WSL.

Note: this assumes the SSH public key has already been generated. See [this article](https://tsuji.tech/ssh-remote-windows/) for details.

```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh -4 -p 22222 wsluser@<hostname> "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

To simplify the connection, you can also add the following to the client's `~/.ssh/config`.

```bash
Host remote-wsl
  HostName <hostname>  # or <hostname>.local or <ip-address>
  Port 22222
  User wsluser
  AddressFamily inet   # Force IPv4
```

This allows you to easily connect with the following command.

```bash
# You can connect with the following instead of ssh -4 -p 22222 wsluser@<hostname>
ssh remote-wsl
```

### Troubleshooting

Isolating the problem step by step makes the root cause easier to find:

- Remote WSL: check that sshd is listening on 22222 with `ss -tlnp | grep 22222`
- Remote Windows: check the forwarding configuration with `netsh interface portproxy show v4tov4`
- Remote Windows: try a local connection to WSL with `ssh -p 22222 wsluser@localhost`
- Client: try SSH into the remote Windows machine with `ssh username@hostname`
- Client: try the external connection with `ssh -4 -v -p 22222 wsluser@<Windows-IP>` (use `-v` for verbose logs)

### Automatically Updating the WSL IP Address

WSL runs on a virtual NIC, and its IP changes every time it starts, so the Windows portproxy setting also needs to be updated accordingly.

Create the following update PowerShell script on the remote Windows machine.

```powershell
# update-wsl-portproxy.ps1
$wslIp = (wsl hostname -I).Trim().Split(' ')[0]
netsh interface portproxy delete v4tov4 listenport=22222 listenaddress=0.0.0.0 2>$null
netsh interface portproxy add v4tov4 listenport=22222 listenaddress=0.0.0.0 connectport=22222 connectaddress=$wslIp
Write-Host "Forwarded 22222 -> $wslIp:22222"
```

Because the script uses `netsh`, it must be **run from an Administrator PowerShell on the Windows side**. It does not work inside WSL. There are two common ways to run it.

#### Method 1: Run Automatically at Windows Logon via Task Scheduler

The WSL IP may change every time Windows restarts, so it is convenient to update it automatically at logon.

1. Run the following in an Administrator PowerShell to register the task (replace `C:\Scripts\update-wsl-portproxy.ps1` with the actual path where you placed the script).

   ```powershell
   $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File C:\Scripts\update-wsl-portproxy.ps1"
   $trigger = New-ScheduledTaskTrigger -AtLogOn
   $principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -RunLevel Highest
   Register-ScheduledTask -TaskName "Update WSL PortProxy" -Action $action -Trigger $trigger -Principal $principal
   ```

2. After registration, you can find "Update WSL PortProxy" in the Task Scheduler GUI (`taskschd.msc`).
3. To verify it works, right-click the task and choose "Run" to start it manually.

Note: because the script calls `wsl hostname -I`, WSL will be started automatically even if it was stopped.

#### Method 2: Run Manually After Restarting WSL

The IP may have changed immediately after restarting WSL with `wsl --shutdown` or similar. In that case, run the script manually from an Administrator PowerShell.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File C:\Scripts\update-wsl-portproxy.ps1
```

After running, check `netsh interface portproxy show v4tov4`; if the forwarding destination IP is updated to the latest WSL IP, you are done.
