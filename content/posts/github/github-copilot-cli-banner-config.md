---
title: "GitHub Copilot CLI Configuration for Banner"
description: ""
date: 2026-02-20T09:00:00+09:00
lastmod:
draft: false
---

## GitHub Copilot CLI Configuration for Banner

1. Open `~/.copilot/config.json` file
2. Edit the config `"banner": "always"`:

```json
{
  "banner": "always",
  "render_markdown": true,
  "model": "claude-sonnet-4.6",
  "reasoning_effort": "medium"
}
```

then the pretty banner will be always shown when you run `copilot` command in terminal:

```bash
┌──                                                                         ──┐
│                                                           ▄██████▄          │
    Welcome to GitHub                                   ▄█▀▀▀▀▀██▀▀▀▀▀█▄
    █████┐ █████┐ █████┐ ██┐██┐     █████┐ ██████┐     ▐█ ██   ▐▌      █▌
   ██┌───┘██┌──██┐██┌─██┐██│██│    ██┌──██┐└─██┌─┘     ▐█▄█   ▄██▄    ▄█▌
   ██│    ██│  ██│█████┌┘██│██│    ██│  ██│  ██│      ▄▄███████▀▀███████▄▄
   ██│    ██│  ██│██┌──┘ ██│██│    ██│  ██│  ██│     ████     ▄  ▄     ████
   └█████┐└█████┌┘██│    ██│██████┐└█████┌┘  ██│     ████     █  █     ████
    └────┘ └────┘ └─┘    └─┘└─────┘ └────┘   └─┘     ▀███▄            ▄███▀
│                              CLI Version 0.0.412      ▀▀████████████▀▀      │
└──                                                                         ──┘
```
