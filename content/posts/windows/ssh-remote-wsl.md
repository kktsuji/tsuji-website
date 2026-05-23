---
title: "SSH into WSL on a Remote Windows Machine"
description: ""
date: 2026-05-23T16:30:00+09:00
lastmod:
draft: false
---

To SSH from a client into WSL on a remote Windows machine, use the Windows port forwarding feature.

## Prerequisites

You should already be able to SSH into the remote Windows machine as described in [this article](https://tsuji.tech/ssh-remote-windows/). If you have not set this up yet, please establish SSH access to the remote Windows machine first by following that guide.

## Install the OpenSSH Server on the Remote WSL

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install openssh-server
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

## Windows Configuration

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

## Connecting via SSH from the Client to the Remote WSL

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

## Troubleshooting

Isolating the problem step by step makes the root cause easier to find:

- Remote WSL: check that sshd is listening on 22222 with `ss -tlnp | grep 22222`
- Remote Windows: check the forwarding configuration with `netsh interface portproxy show v4tov4`
- Remote Windows: try a local connection to WSL with `ssh -p 22222 wsluser@localhost`
- Client: try SSH into the remote Windows machine with `ssh username@hostname`
- Client: try the external connection with `ssh -4 -v -p 22222 wsluser@<Windows-IP>` (use `-v` for verbose logs)

## Automatically Updating the WSL IP Address

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

### Method 1: Run Automatically at Windows Logon via Task Scheduler

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

### Method 2: Run Manually After Restarting WSL

The IP may have changed immediately after restarting WSL with `wsl --shutdown` or similar. In that case, run the script manually from an Administrator PowerShell.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File C:\Scripts\update-wsl-portproxy.ps1
```

After running, check `netsh interface portproxy show v4tov4`; if the forwarding destination IP is updated to the latest WSL IP, you are done.
