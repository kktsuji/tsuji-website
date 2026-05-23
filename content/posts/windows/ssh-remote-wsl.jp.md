---
title: "リモートWindowsのWSLへSSH接続"
description: ""
date: 2026-05-23T16:30:00+09:00
lastmod:
draft: false
---

クライアントからリモートWindowsのWSLへSSH接続をする場合、Windowsのポートフォワーディング機能を利用します。

## 前提

[この記事](https://tsuji.tech/jp/ssh-remote-windows/)でリモートWindowsへのSSH接続ができていること。未設定の場合は、先にこちらを参考にしてリモートWindowsへのSSH接続を確立してください。

## リモートのWSLへOpenSSHサーバをインストール

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install openssh-server
```

`Port 22222`など、Windows側(22)と被らないポートに変更：

```bash
sudo vim /etc/ssh/sshd_config
```

SSHサーバを再起動：

```bash
sudo service ssh restart
```

sshdが22222で待ち受けているか確認：

```bash
ss -tlnp | grep 22222

# 出力例
# LISTEN 0      128           0.0.0.0:22222      0.0.0.0:*
# LISTEN 0      128              [::]:22222         [::]:*
```

この設定が完了したら、リモートWindowsからWSLへSSH接続できることを確認します。

```powershell
# WSLのパスワードが必要
ssh -p 22222 wsluser@localhost
```

## Windowsの設定

以下、リモートWindowsの管理者権限のPowerShellで実行します。

### portproxyの待ち受けポート設定

WSLのIPアドレスを取得し、Windowsのportproxyでポートフォワーディングを設定します。

WSLはIPアドレスが２つ以上表示される（例：IPv4とIPv6, Docker）ことがあるため、最初のIPアドレス（IPv4）を取得します。

```powershell
# WSLのIPアドレス（IPv4）を取得
$wslIp = (wsl hostname -I).Trim().Split(' ')[0]

# Windowsのportproxyでポートフォワーディングを設定
netsh interface portproxy add v4tov4 listenport=22222 listenaddress=0.0.0.0 connectport=22222 connectaddress=$wslIp

# 確認
# Listen on ipv4: 0.0.0.0:22222 → Connect to ipv4: 172.x.x.x:22222 のように表示されればOK
netsh interface portproxy show v4tov4
```

### ファイアウォールでport 22222を許可

Windows Defenderファイアウォールでこのポートを開けると、外部からWSLのSSHサーバへ接続できるようになります。

```powershell
New-NetFirewallRule -DisplayName "WSL SSH" -Direction Inbound -LocalPort 22222 -Protocol TCP -Action Allow
```

## クライアントからリモートのWSLへSSH接続

以下で接続を確認します。

注意：IPv4で接続するための`-4`オプションを明示的に指定します。無しの場合、環境によってはIPv6が使用され接続に失敗する可能性があります。

```powershell
ssh -4 -p 22222 wsluser@<hostname>
```

接続が成功すれば、リモートWindowsのWSLへSSH接続できています。

パスワードなしで接続したい場合は、SSHキーを生成してリモートWindowsのWSLに公開鍵を配置してください。

注意：SSH公開鍵は既に生成済みの前提です。詳細は[この記事](https://tsuji.tech/jp/ssh-remote-windows/)を参照。

```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh -4 -p 22222 wsluser@<hostname> "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

また、接続簡略化のために、クライアント側の`~/.ssh/config`に以下の設定を追加することもできます。

```bash
Host remote-wsl
  HostName <hostname>  # or <hostname>.local or <ip-address>
  Port 22222
  User wsluser
  AddressFamily inet   # IPv4を強制
```

これにより、以下のコマンドで簡単にSSH接続できるようになります。

```bash
# ssh -4 -p 22222 wsluser@<hostname> の代わりに以下で接続可能
ssh remote-wsl
```

## トラブルシューティング

段階的に切り分けると原因が見つけやすいです：

- リモートWSL：`ss -tlnp | grep 22222` でsshdが22222で待ち受けているか確認
- リモートWindows：`netsh interface portproxy show v4tov4` で転送設定を確認
- リモートWindows：`ssh -p 22222 wsluser@localhost` でWSLへのローカル経由の接続を試す
- クライアント：`ssh username@hostname` でリモートWindowsへのSSH接続を試す
- クライアント：`ssh -4 -v -p 22222 wsluser@<WindowsのIP>` で外部経由を試す (`-v`で詳細なログを表示)

## WSLのIPアドレス自動更新

WSLは仮想NIC上で動作し、起動するたびにIPが変わるため、Windowsのportproxy設定も更新する必要があります。

リモートWindowsで以下の更新用PSスクリプトを作成しておきます。

```powershell
# update-wsl-portproxy.ps1
$wslIp = (wsl hostname -I).Trim().Split(' ')[0]
netsh interface portproxy delete v4tov4 listenport=22222 listenaddress=0.0.0.0 2>$null
netsh interface portproxy add v4tov4 listenport=22222 listenaddress=0.0.0.0 connectport=22222 connectaddress=$wslIp
Write-Host "Forwarded 22222 -> $wslIp:22222"
```

スクリプトは `netsh` を使うため、**Windows側で管理者権限のPowerShellから実行**する必要があります。WSL内では動きません。実行するタイミングとして、以下の２通りの方法があります。

### 方法1：Windowsログオン時にタスクスケジューラで自動実行

Windows再起動のたびにWSLのIPが変わる可能性があるため、ログオン時に自動で更新するのが便利です。

1. 管理者権限のPowerShellで以下を実行し、タスクを登録します（`C:\Scripts\update-wsl-portproxy.ps1` は実際のスクリプト配置パスに置き換え）。

   ```powershell
   $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File C:\Scripts\update-wsl-portproxy.ps1"
   $trigger = New-ScheduledTaskTrigger -AtLogOn
   $principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -RunLevel Highest
   Register-ScheduledTask -TaskName "Update WSL PortProxy" -Action $action -Trigger $trigger -Principal $principal
   ```

2. 登録後、タスクスケジューラのGUI（`taskschd.msc`）から「Update WSL PortProxy」を確認できます。
3. 動作確認したい場合は、タスクを右クリック →「実行する」で手動起動できます。

注意：スクリプト内で `wsl hostname -I` を呼ぶため、WSLが停止していても自動で起動されます。

### 方法2：WSL再起動後に手動実行

`wsl --shutdown` などでWSLを再起動した直後は、IPが変わっている可能性があります。その場合は、管理者権限のPowerShellで手動実行します。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File C:\Scripts\update-wsl-portproxy.ps1
```

実行後、`netsh interface portproxy show v4tov4` で転送先IPが最新のWSL IPに更新されていれば成功です。
