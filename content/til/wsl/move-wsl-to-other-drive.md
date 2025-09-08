---
title: 'Move WSL from C Drive to Other Drive'
description: ''
date: 2025-08-03T15:00:00+09:00
lastmod:
draft: false
---

## Move WSL from C Drive to Other Drive

Move WSL in `\\wsl$` to `W:\WSL`.

1. Open PowerShell as Administrator
2. Shutdown WSL `wsl --shutdown`
3. Check wsl version `wsl --list --verbose`
4. Create a new directory on the target drive `mkdir W:\WSL`
5. Export the WSL distribution `Ubuntu-22.04` to the new directory as a tar file `wsl --export Ubuntu-22.04 W:\WSL\Ubuntu-22.04.tar`
6. Unregister the WSL distribution `wsl --unregister Ubuntu-22.04`
7. Import the WSL distribution from the tar file to the new directory `wsl --import Ubuntu-22.04 W:\WSL\Ubuntu-22.04 W:\WSL\Ubuntu-22.04.tar --version 2`
8. Set the default WSL distribution to the newly imported one `wsl --set-default Ubuntu-22.04`

## Login User Settings

The new WSL distribution's login user is set to the root user by default. To change it to your user:

1. Open the WSL distribution `wsl -d Ubuntu-22.04`
2. Change the login user to your user `vim /etc/wsl.conf` and add the following lines:

```ini
[user]
default=your_username
```

3. Save and exit the editor
4. Restart the WSL distribution `wsl --shutdown` and then `wsl -d Ubuntu-22.04`
