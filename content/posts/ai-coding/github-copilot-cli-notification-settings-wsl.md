---
title: "Github Copilot CLI Notification Settings in WSL"
description: ""
date: 2026-03-12T09:00:00+09:00
lastmod:
math: true
draft: false
---

## Overview

In this article, I'll show you how to set up Windows Toast notifications for Github Copilot CLI running in WSL using a custom notification script and the BurntToast PowerShell module.

- Install BurntToast in Windows Powershell
- Create a notification script in WSL that sends notifications via PowerShell
- Configure Github Copilot CLI hooks to trigger the notification script on specific events (e.g., when a session ends or when a prompt is submitted)
- Test the setup by running a Github Copilot CLI command and confirming you receive a Windows Toast notification

![img](https://img.tsuji.tech/github-copilot-cli-notification-settings-wsl-0.jpg)

## Install BurntToast in Powershell

Install the BurntToast module in Powershell to send Windows Toast notifications from WSL.

```Powershell
Install-Module -Name BurntToast -Force -Scope CurrentUser
```

Confirm your execution policy allows running scripts:

```Powershell
Get-ExecutionPolicy -Scope CurrentUser
```

If the execution policy is too restrictive (e.g., `Restricted`), set it to `RemoteSigned`:

```Powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

You can now send test notifications from Powershell to confirm BurntToast is working:

```Powershell
Import-Module BurntToast
New-BurntToastNotification -Text "Test Notification", "BurntToast is working!"
```

## (Optional) Put Custom Logo for Notifications

You can use a custom logo for the notifications by placing an image file (e.g., `logo.png`) in a Windows directory. In this article, we put the logo in `D:\your\logo\path\logo.png`. Update the `ICON` variable in the script below with the path to your logo.

You can test the notification with the custom logo:

```Powershell
Import-Module BurntToast
New-BurntToastNotification -Text "Test Notification", "BurntToast is working!" -AppLogo "D:\your\logo\path\logo.png"
```

## Create Notification Script in WSL

Create a script file for example `vim ~/.bin/copilot-notify.sh` and add the following content:

```bash
#!/bin/bash
# copilot-notify.sh
# Sends a Windows Toast notification when Copilot CLI hooks are triggered.
# Copilot CLI passes hook data as JSON via stdin.
# The hook event name is passed via COPILOT_HOOK_EVENT env var.

# Ensure common binaries are available
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH"

# Read JSON payload from stdin
STDIN=$(cat)

# Debug log — uncomment to troubleshoot
#{
#  echo "=== $(date) ==="
#  echo "COPILOT_HOOK_EVENT: $COPILOT_HOOK_EVENT"
#  echo "STDIN: $STDIN"
#} >> /tmp/copilot-hook-debug.log 2>&1

# Set notification title and message based on hook event
case "$COPILOT_HOOK_EVENT" in
  "sessionEnd")
    TITLE="Copilot - Done"
    MESSAGE="Session completed!"
    ;;
  "preToolUse")
    TITLE="Copilot - Action Needed"
    MESSAGE="Waiting for your input!"
    ;;
  "errorOccurred")
    TITLE="Copilot - Error"
    MESSAGE="An error occurred!"
    ;;
  *)
    TITLE="Copilot"
    MESSAGE="Notification"
    ;;
esac

# Convert WSL icon path to Windows path for PowerShell
ICON="/mnt/d/your/logo/path/logo.png"
WIN_ICON=$(wslpath -w "$ICON" 2>/dev/null)

# Send Windows Toast notification via BurntToast PowerShell module
/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -Command "
Import-Module BurntToast
New-BurntToastNotification -Text '$TITLE', '$MESSAGE' -AppLogo '$WIN_ICON'
" 2>/dev/null

# Fallback: terminal bell in case PowerShell notification fails
echo -e "\a"
```

Make the script executable:

```bash
chmod +x ~/.bin/copilot-notify.sh
```

## Configure Copilot CLI Hooks

### Create hooks.json

Create a hooks configuration file. We'll store it centrally at `~/.copilot/hooks.json` and symlink it into each project:

```json
{
  "version": 1,
  "hooks": {
    "sessionEnd": [
      {
        "type": "command",
        "bash": "/home/your-username/.bin/copilot-notify.sh",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "sessionEnd" }
      }
    ],
    "preToolUse": [
      {
        "type": "command",
        "bash": "/home/kktsuji/.bin/copilot-notify.sh",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "preToolUse" }
      }
    ],
    "errorOccurred": [
      {
        "type": "command",
        "bash": "/home/your-username/.bin/copilot-notify.sh",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "errorOccurred" }
      }
    ]
  }
}
```

Replace `/home/your-username/.bin/copilot-notify.sh` with the actual path to your notification script.

The available hook events are:

| Event                 | Description             |
| --------------------- | ----------------------- |
| `sessionStart`        | Session started         |
| `sessionEnd`          | Session completed       |
| `userPromptSubmitted` | User submitted a prompt |
| `preToolUse`          | Before a tool is used   |
| `postToolUse`         | After a tool is used    |
| `errorOccurred`       | An error occurred       |

For more details on hooks, see the [Using hooks with GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks) documentation.

### Symlink hooks.json into Your Project

Copilot CLI loads hooks from `.github/hooks/hooks.json` in the current working directory. Create a symlink in each project where you want notifications:

```bash
mkdir -p your-project/.github/hooks
ln -s ~/.copilot/hooks.json your-project/.github/hooks/hooks.json
```

This way, you maintain a single `hooks.json` and share it across multiple projects.

## Test with Copilot CLI

Go to your project directory and run the Copilot CLI:

```bash
cd your-project
copilot
```

Then send a small request to trigger the hooks, for example:

```bash
> hi
```

If everything is set up correctly, you should see Windows Toast notifications when:

- The session ends (`sessionEnd`)
- An error occurs (`errorOccurred`)

![img](https://img.tsuji.tech/github-copilot-cli-notification-settings-wsl-0.jpg)

## Debugging

If you don't see notifications, enable the debug logging in `~/.bin/copilot-notify.sh` by uncommenting the debug block:

```bash
# Debug log — uncomment to troubleshoot
{
  echo "=== $(date) ==="
  echo "COPILOT_HOOK_EVENT: $COPILOT_HOOK_EVENT"
  echo "STDIN: $STDIN"
} >> /tmp/copilot-hook-debug.log 2>&1
```

Then check the log at `/tmp/copilot-hook-debug.log`:

```bash
cat /tmp/copilot-hook-debug.log
```

If the log file doesn't exist after running Copilot CLI, the hooks aren't being loaded. Verify that:

1. The symlink is valid: `ls -la your-project/.github/hooks/hooks.json`
2. The hooks.json path is `.github/hooks/hooks.json` (not the project root)
3. The notification script is executable: `ls -la ~/.bin/copilot-notify.sh`

You can also test the script directly:

```bash
echo '{"timestamp":1704614400000}' | COPILOT_HOOK_EVENT=sessionEnd ~/.bin/copilot-notify.sh
```

After confirming the setup works, comment out the debug logging lines to avoid unnecessary logging.
