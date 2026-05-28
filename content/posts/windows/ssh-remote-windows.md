---
title: "SSH into a Remote Windows Machine"
description: ""
date: 2026-05-23T16:00:00+09:00
lastmod:
draft: false
---

## Checking Ping

First, send a ping from the client to the remote Windows machine's IP address to confirm that network connectivity is established.

When the remote PC name is `<hostname>`:

```powershell
# Between Windows machines
ping <hostname>

# Using mDNS (macOS / Linux / WSL, etc.)
ping <hostname>.local
```

You can also use the remote IP address directly:

```powershell
# After checking the IP address on the remote with `ipconfig`
ping <ip-address>
```

### When to use `.local` and when not to

`.local` is a special domain used by mDNS (Multicast DNS, RFC 6762), which allows name resolution within a LAN without going through a DNS server. Choose whether to use it based on the client environment.

When to use `ping <hostname>` (without `.local`):

- The client is Windows and the remote is also Windows (on the same LAN)
  - Resolved by NetBIOS over TCP/IP or LLMNR
- Environments where the PC name is registered on an internal DNS server (e.g. domain-joined PCs)
- Environments where a DNS suffix (e.g. `corp.example.com`) is configured, so `<hostname>` alone is completed into an FQDN

When to use `ping <hostname>.local`:

- Reaching a Windows machine from a macOS / Linux / iOS / Android client
  - Bonjour (macOS) / Avahi (Linux) resolves it via mDNS
- Home LANs or small offices without a DNS server
- Hardened security environments where NetBIOS / LLMNR is disabled
- Mixed environments with IoT devices, Raspberry Pi, etc. where mDNS is standard

Quick reference:

| Client → Remote                      | Recommended                              |
| ------------------------------------ | ---------------------------------------- |
| Windows → Windows (home LAN)         | Either works. Try without `.local` first |
| Windows → Windows (corporate domain) | Without `.local`                         |
| macOS / Linux → Windows              | With `.local`                            |
| WSL → host Windows                   | With `.local` (or `$(hostname).local`)   |

Note that to use `.local` on the Windows side, you need either Bonjour Print Services or the built-in mDNS available in Windows 10 1803 or later. On older versions of Windows, `.local` may not work.

## When Ping Doesn't Work

### Check the Firewall

The Windows firewall on the remote machine may be blocking ICMP (ping). Check it as follows.

1. On the remote Windows machine, open "Windows Defender Firewall with Advanced Security".
2. Click "Inbound Rules" on the left.
3. Look for "File and Printer Sharing (Echo Request - ICMPv4-In)".
4. Confirm that its state is "Enabled" and "Allow".
5. If it is disabled or blocked, right-click and choose "Enable Rule".
6. Likewise, check "File and Printer Sharing (Echo Request - ICMPv6-In)" if you are on IPv6.

### Check the Router

Your home or office router may also be blocking ICMP. Access the router's admin page and check the firewall and security settings. In particular, if there is an option such as "Allow Ping response", enable it.

### Check Antivirus Software

Some antivirus or security software blocks ICMP. Check the settings of the security software installed on the remote Windows machine and allow ICMP if necessary.

## Setting Up the SSH Server

Once ping is working, set up the SSH server on the remote machine. From Windows 10 onward, the OpenSSH server is built in and can be enabled as follows.

1. Open "Settings" → "Apps" → "Optional features".
2. Click "Add a feature".
3. Search for "OpenSSH Server", select it, and click "Install".

Alternatively, open PowerShell as Administrator and run the following commands.

```powershell
# Check the installation status of the OpenSSH Server
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Server*'
```

How to read the result:

- If it shows `State : Installed`: already installed. Proceed to configuration.
- If it shows `State : NotPresent`: not installed.

To install:

```powershell
Add-WindowsCapability -Online -Name "OpenSSH.Server~~~~0.0.1.0"
```

After installation, configure it as follows.

```powershell
# Set the service to start automatically
Set-Service -Name sshd -StartupType 'Automatic'

# Start the service now
Start-Service sshd

# Check the status
Get-Service -Name sshd
```

If the status shows `Status: Running`, the SSH server is up and running on the remote PC.

## Connecting via SSH from the Client

To SSH into the remote Windows machine from the client, use the following command.

```bash
ssh <username>@<hostname>  # or <username>@<hostname>.local
```

Specify the account name on the remote Windows machine as the username. On a successful connection, you can access the remote Windows command prompt or PowerShell.

On the first connection, you will be prompted to verify the host key, so check the displayed fingerprint and type "yes".

In this state, you have to enter your password every time you connect. If you want to connect without a password, generate an SSH key and place the public key on the remote Windows machine.

Here is an example of generating an SSH key on the client.

```powershell
# Generate an SSH key on the client
ssh-keygen -t ed25519
```

This creates `~/.ssh/id_ed25519` (private key) and `~/.ssh/id_ed25519.pub` (public key). By appending the public key to `.ssh/authorized_keys` under the user profile on the remote Windows machine, you can connect via SSH without a password.

```powershell
# Copy the public key to the remote Windows machine
type ~/.ssh/id_ed25519.pub | ssh <username>@<hostname> "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

Or you can copy it directly with the following commands.

```powershell
# SSH into the remote
ssh <username>@<hostname>

# Create the ".ssh" folder on the remote
New-Item -ItemType Directory -Path "$HOME\.ssh" -Force

# Paste the local public key into the remote's authorized_keys
Set-Content -Path "$HOME\.ssh\authorized_keys" -Value "paste the copied public key here"
```

Finally, set the appropriate permissions on the public key on the remote side.

```powershell
# Set permissions on the public key (grant Full Control to Administrators and the user via Windows ACL)
icacls "$HOME\.ssh\authorized_keys" /inheritance:r /grant:r "Administrators:F" /grant:r "${env:USERNAME}:F"
```

### When Connecting to the Remote as an Administrator

Depending on the account settings on the remote, you may automatically be elevated to administrator privileges after connecting via SSH.

In that case, the public key needs to be placed in a system-wide location, not in the administrator's home directory `.ssh/authorized_keys`.

```powershell
# Create the system-wide folder for storing the public key
New-Item -ItemType Directory -Path "$env:ProgramData\ssh" -Force

# Paste the copied public key into the administrators' public key file
Set-Content -Path "$env:ProgramData\ssh\administrators_authorized_keys" -Value "paste the copied public key here"

# Set permissions on the public key (grant Full Control to Administrators and SYSTEM)
icacls "$env:ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant:r "Administrators:F" /grant:r "SYSTEM:F"
```

## SSH Configuration on the Client

To simplify SSH connections on the client side, you can add the remote Windows settings to the `~/.ssh/config` file.

```bash
Host remote-win
  HostName <hostname>  # or <hostname>.local or <ip-address>
  User <username>
```

This allows you to easily connect via SSH with the following command.

```bash
# You can connect with the following instead of ssh <username>@<hostname>
ssh remote-win
```

## Set PowerShell as the Default for SSH Connections

Check the PowerShell path on the remote Windows machine.

```powershell
# For Command Prompt
where powershell

# For PowerShell
Get-Command powershell | Select-Object -ExpandProperty Source
```

It is usually `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`.

Run the following command in PowerShell with administrator privileges to change the default shell for SSH connections to PowerShell.

```powershell
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
```
