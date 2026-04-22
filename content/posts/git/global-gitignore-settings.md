---
title: "Global Gitignore Settings"
description: ""
date: 2026-04-22T09:00:00+09:00
lastmod:
draft: False
---

Set up global gitignore settings to ignore files across all repositories on your system.

Bash:

```bash
# Set up global gitignore file
git config --global core.excludesfile ~/.gitignore_global

# Create the global gitignore file
touch ~/.gitignore_global

# Add patterns to the global gitignore file
echo ".local-tmp/" >> ~/.gitignore_global

# Verify the global gitignore settings
git config --global core.excludesfile
cat ~/.gitignore_global
```

PowerShell:

```PowerShell
# Set up global gitignore file
git config --global core.excludesfile $env:USERPROFILE\.gitignore_global

# Create the global gitignore file
New-Item -ItemType File -Path $env:USERPROFILE\.gitignore_global -Force

# Add patterns to the global gitignore file
Add-Content -Path $env:USERPROFILE\.gitignore_global -Value ".local-tmp/"

# Verify the global gitignore settings
git config --global core.excludesfile
Get-Content -Path $env:USERPROFILE\.gitignore_global
```
