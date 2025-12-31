---
title: "Disable Windows Environment Variables in WSL"
description: ""
date: 2025-12-31T10:00:00+09:00
lastmod:
draft: false
---

By default, WSL imports Windows environment variables into the WSL environment. If you want to disable this behavior, you can do so by modifying the WSL configuration file.

You can see the current environment variables in WSL.

```bash
echo $PATH
```

## Steps to Disable Windows Environment Variables in WSL

1. Open or create the WSL configuration file `sudo vim /etc/wsl.conf`.
2. Add the following lines:

```ini
[interop]
enabled = true # Enable to run Windows executables (.exe files) from WSL
appendWindowsPath = false # Disable importing Windows PATH environment variables
```

3. Save the file and exit the editor.
4. Restart WSL by running `wsl --shutdown` in PowerShell or Command Prompt.

Then you can confirm that Windows environment variables are no longer imported.

```bash
echo $PATH
```

## Setup the Alias for Windows Executables (.exe files)

If you disabled the Windows PATH import, you should input the full path to run .exe files instead of the filename only.

- When appendWindowsPath = false: `explorer.exe .`
- When appendWindowsPath = true: `/mnt/c/Windows/explorer.exe .`

You can set up an alias in your shell configuration file to make it easier to run .exe files.

1. Open your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`).
2. Add the following line to create an alias like:

```bash
alias explorer='/mnt/c/Windows/explorer.exe'
alias code='/mnt/c/Users/YourUsername/AppData/Local/Programs/Microsoft\ VS\ Code/Code.exe'
alias otherapp='/mnt/c/Path/To/YourApp.exe'
```

3. Save the file and reload the configuration by running `source ~/.bashrc` or `source ~/.zshrc`.
