---
title: "「COM Surrogateによってファイルが開かれているため、操作を完了できません」を解決する：WindowsのCOM Surrogateファイルロック問題"
description: ""
date: 2025-12-27T16:00:00+09:00
lastmod:
draft: false
---

Windowsでファイルを削除する際、COM Surrogate (dllhost.exe) がファイルをロックしてしまい、削除できない問題が発生することがあります。エラーメッセージは「COM Surrogateによってファイルが開かれているため、操作を完了できません」です。

## エクスプローラを再起動する

1. タスクマネージャーを開く(`Ctrl`+`Shift`+`Esc`)。
2. プロセスタブで`Windows Explorer`を見つけて選択する。
3. 右下の`Restart`をクリックする。

## COM Surrogateプロセスを終了する

1. タスクマネージャーを開く(`Ctrl`+`Shift`+`Esc`)。
2. プロセスタブで`COM Surrogate`または`dllhost.exe`プロセスを探す。
3. 各`COM Surrogate`プロセスを選択して`タスクの終了`をクリックする。
