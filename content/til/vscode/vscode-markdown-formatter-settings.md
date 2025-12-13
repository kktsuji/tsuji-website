---
title: "VSCode Markdown Formatter Settings"
description: ""
date: 2024-12-16T21:00:00+09:00
lastmod:
draft: false
---

1. Install extension (markdown-all-in-one, markdownlint, etc.)
2. Open VSCode settings.json
   - File > Preferences > Settings or `Ctrl + ,` then click the `Open Setting (JSON)` icon on the top right corner
   - Or open `%APPDATA%\Code\User\settings.json`
3. Add the following settings to the settings.json file:

```json
{
  "[markdown]": {
    "editor.defaultFormatter": "yzhang.markdown-all-in-one"
  },

  "editor.formatOnPaste": true, // optional
  "editor.formatOnSave": true, // optional
  "editor.formatOnType": true // optional
}
```
