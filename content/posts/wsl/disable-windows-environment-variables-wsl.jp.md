---
title: "WSLでWindows環境変数を無効化する"
description: ""
date: 2025-12-31T10:00:00+09:00
lastmod:
draft: false
---

デフォルトでは、WSLはWindows環境変数をWSL環境にインポートします。この動作を無効化したい場合は、WSL設定ファイルを変更することで実現できます。

WSLで現在の環境変数を確認できます。

```bash
echo $PATH
```

## WSLでWindows環境変数を無効化する手順

1. WSL設定ファイルを開くか作成します`sudo vim /etc/wsl.conf`。
2. 以下の行を追加します:

```ini
[interop]
enabled = true # WSLからWindowsの実行可能ファイル(.exeファイル)を実行できるようにする
appendWindowsPath = false # WindowsのPATH環境変数のインポートを無効化する
```

3. ファイルを保存してエディタを終了します。
4. PowerShellまたはCommand Promptで`wsl --shutdown`を実行してWSLを再起動します。

その後、Windows環境変数がインポートされなくなったことを確認できます。

```bash
echo $PATH
```

## Windows実行可能ファイル(.exeファイル)のエイリアス設定

WindowsのPATHインポートを無効化した場合、.exeファイルを実行するにはファイル名だけでなくフルパスを入力する必要があります。

- appendWindowsPath = falseの場合:`explorer.exe .`
- appendWindowsPath = trueの場合:`/mnt/c/Windows/explorer.exe .`

.exeファイルを簡単に実行できるように、シェル設定ファイルでエイリアスを設定できます。

1. シェル設定ファイル(例:`~/.bashrc`または`~/.zshrc`)を開きます。
2. 次のようなエイリアスを作成する行を追加します:

```bash
alias explorer='/mnt/c/Windows/explorer.exe'
alias code='/mnt/c/Users/YourUsername/AppData/Local/Programs/Microsoft\ VS\ Code/Code.exe'
alias otherapp='/mnt/c/Path/To/YourApp.exe'
```

3. ファイルを保存し、`source ~/.bashrc`または`source ~/.zshrc`を実行して設定を再読み込みします。
