---
title: "VSCode Markdownフォーマッター設定"
description: ""
date: 2024-12-16T21:00:00+09:00
lastmod:
draft: false
---

1. エクステンションをインストールする（markdown-all-in-one、markdownlintなど）
2. VSCodeのsettings.jsonを開く
   - File > Preferences > Settingsまたは`Ctrl`+`,`を押して、右上の`Open Setting (JSON)`アイコンをクリックする
   - または`%APPDATA%\Code\User\settings.json`を開く
3. settings.jsonファイルに以下の設定を追加する：

```json
{
  "[markdown]": {
    "editor.defaultFormatter": "yzhang.markdown-all-in-one"
  },

  "editor.formatOnPaste": true, // オプション
  "editor.formatOnSave": true, // オプション
  "editor.formatOnType": true // オプション
}
```
