---
title: 'Block Websites on PC'
description: 'Today I Learned post about how to block websites on PC.'
date: 2024-05-30T20:29:55+09:00
lastmod: 
draft: false
---

## Windows

1. Backup ``C:\Windows\System32\drivers\etc\hosts``
2. Open ``hosts`` file and add localhost IP adress ``127.0.0.1`` and domains of websites that you want to block

```bash
# Block Lists
127.0.0.1 twitter.com
127.0.0.1 x.com
```

3. Save it

All websites you added in ``hosts`` will be blocked on any web browsers.

Save your time!

(Note: Any methods, such as ``ping`` command, also will be blocked on this PC)
