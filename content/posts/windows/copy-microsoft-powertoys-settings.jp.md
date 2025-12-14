---
title: "Microsoft PowerToysの設定をコピーする"
description: ""
date: 2025-10-18T16:00:00+09:00
lastmod:
draft: false
---

## Microsoft PowerToysの設定をコピーする

ファイルエクスプローラーで`%LocalAppData%\Microsoft\PowerToys\`を開きます。各PowerToysモジュールの設定ファイルが含まれています。

- 希望する`settings.json`をコピーする
- 別のPCの同じパスに貼り付ける
- PowerToysが実行中の場合は再起動する

例：

各jsonファイルの内容を確認して理解できます。

- PowerToysの一般設定：`%LocalAppData%\Microsoft\PowerToys\settings.json`
- Keyboard Managerのリマップ設定：`%LocalAppData%\Microsoft\PowerToys\Keyboard Manager\default.json`
- など
