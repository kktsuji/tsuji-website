---
title: "WSLをCドライブから他のドライブへ移動"
description: ""
date: 2025-08-03T15:00:00+09:00
lastmod:
draft: false
---

## WSLをCドライブから他のドライブに移動

`\\wsl$`にあるWSLを`W:\WSL`に移動する。

1. PowerShellを管理者として開く
2. WSLをシャットダウン `wsl --shutdown`
3. wslバージョンを確認 `wsl --list --verbose`
4. ターゲットドライブに新しいディレクトリを作成 `mkdir W:\WSL`
5. WSLディストリビューション`Ubuntu-22.04`を新しいディレクトリにtarファイルとしてエクスポート `wsl --export Ubuntu-22.04 W:\WSL\Ubuntu-22.04.tar`
6. WSLディストリビューションの登録を解除 `wsl --unregister Ubuntu-22.04`
7. tarファイルから新しいディレクトリにWSLディストリビューションをインポート `wsl --import Ubuntu-22.04 W:\WSL\Ubuntu-22.04 W:\WSL\Ubuntu-22.04.tar --version 2`
8. デフォルトのWSLディストリビューションを新しくインポートしたものに設定 `wsl --set-default Ubuntu-22.04`

## ログインユーザー設定

新しいWSLディストリビューションのログインユーザーはデフォルトでrootユーザーに設定されている。自分のユーザーに変更するには：

1. WSLディストリビューションを開く `wsl -d Ubuntu-22.04`
2. ログインユーザーを自分のユーザーに変更 `vim /etc/wsl.conf`して以下の行を追加：

```ini
[user]
default=your_username
```

3. 保存してエディタを終了
4. WSLディストリビューションを再起動 `wsl --shutdown`してから `wsl -d Ubuntu-22.04`
