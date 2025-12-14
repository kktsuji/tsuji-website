---
title: "Install and Uninstall WSL"
description: ""
date: 2025-02-01T16:00:00+09:00
lastmod:
draft: false
---

## Prerequisites

1. Open Control Panel > Programs > Turn Windows Features on or off
2. Turn on:
   - Windows Subsystem for Linux
   - Virtual Machine Platform
   - (Hyper-V is not necessary)

## Install WSL

1. Open PowerShell as Administrator
2. Run the following command to install WSL2:

```powershell
# Install WSL2
wsl --install

# Update WSL
wsl --update

# Set default version to WSL2
wsl --set-default-version 2

# List available distributions
wsl -l -o

# Install Ubuntu 22.04
wsl --install -d Ubuntu-22.04
```

Other commands we often use:

```powershell
# Help
wsl --help

# Set default distribution
wsl --set-default Ubuntu-22.04

# Show installed distributions
wsl -l -v

# Shutdown WSL
wsl --shutdown
```

## Uninstall WSL distributions

1. Shutdown WSL `wsl --shutdown`
2. Confirm the distribution stopped `wsl -l -v`
3. Settings > Apps > Installed apps > Ubuntu-22.04 > Uninstall

## References

- [Manual installation steps for older versions of WSL - Windows Learn](https://learn.microsoft.com/en-us/windows/wsl/install-manual)
- [How to install Linux on Windows with WSL - Windows Learn](https://learn.microsoft.com/en-us/windows/wsl/install)
