---
title: 'Remap Caps Lock to Ctrl via Registry Editor on Windows'
description: ''
date: 2025-10-21T18:00:00+09:00
lastmod: 
draft: false
---

## Remap Caps Lock to Ctrl via Registry Editor on Windows

1. Press `Win + R`, type `regedit`, and press `Enter` to open the Registry Editor.
2. Export the current registry settings as a backup (File > Export > Select `all` export range > Save as .reg file).
3. Navigate to the following path:

```text
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout
```

4. Right-click on the right pane, select `New` > `Binary Value`, and name it `Scancode Map`.
5. Double-click on `Scancode Map` and enter the following binary data to remap Caps Lock to Ctrl:

```text
00 00 00 00 00 00 00 00
02 00 00 00 1D 00 3A 00
00 00 00 00
```

| Byte    | Value                   | Description                                   |
| ------- | ----------------------- | --------------------------------------------- |
| 8 bytes | 00 00 00 00 00 00 00 00 | Header (always these values)                  |
| 4 bytes | 02 00 00 00             | Number of mappings (1 mapping + 1 terminator) |
| 4 bytes | 1D 00 3A 00             | Map Caps Lock (0x3A) to Left Ctrl (0x1D)      |
| 4 bytes | 00 00 00 00             | Terminator (always these values)              |

6. Click `OK` to save the changes.
7. Close the Registry Editor.
8. Restart your computer for the changes to take effect.

If you want to revert the changes, you can delete the `Scancode Map` entry in the Registry Editor. Another way is to import the backup `.reg` file you created in step 2 in the Registry Editor (File > Import) (you can also apply it to double-click `.reg` file).
