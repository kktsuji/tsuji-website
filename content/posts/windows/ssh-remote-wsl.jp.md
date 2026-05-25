---
title: "リモートWindowsのWSLへSSH接続"
description: ""
date: 2026-05-23T16:30:00+09:00
lastmod:
draft: false
---

クライアントからリモートWindowsのWSLへSSH接続をする場合、以下のどちらかを使用します。

1. SSHのJumphost（推奨）
2. Windowsのポートフォワーディング機能

## 前提

[この記事](https://tsuji.tech/jp/ssh-remote-windows/)でリモートWindowsへのSSH接続ができていること。未設定の場合は、先にこちらを参考にしてリモートWindowsへのSSH接続を確立してください。

## リモートのWSLへOpenSSHサーバをインストール

どちらの方法を用いる場合も、リモートWindowsのWSL側でOpenSSHサーバをインストールし、Windows側と被らないポートで待ち受ける必要があります。

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install openssh-server -y
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

## Windowsの設定（Jumphostを用いる場合）

リモートWindowsのSSHサーバをJumphostとして利用し、SSHのProxyJump機能を用いてクライアントからリモートのWSLへ接続する方法です。

ポートフォワーディングを用いる方法と比べて構成がシンプルなため、こちらの方法を推奨します。

### ミラーモードの前提条件

ミラーモードを使用する場合は以下が必要です：

- ホストOS：Windows 11 22H2 以降
- WSLバージョン：WSL v2.0.4 以上 `(wsl --versionで確認可能)`

### ホスト側のWSL設定

ホストの `C:\Users\<username>\.wslconfig` へ以下を追加します：

```ini
[wsl2]
networkingMode=mirrored
vmIdleTimeout=-1

[experimental]
hostAddressLoopback=true
```

- networkingMode=mirrored：WSLがホストと同じネットワークに直接接続されるため、WSLのIPアドレスがホストと同じになります。これにより、クライアントから直接WSLへSSH接続できるようになります。
- hostAddressLoopback=true：ミラーモード前提のexperimental設定で、ホストに割り当てられているIPアドレスを使って、コンテナ（WSL）⇔ホスト間で接続できるようにするオプションです。これにより、ホストのIPアドレスを使ってWSLへSSH接続できるようになります。なおサポートされるのはホストに割り当てられた IPv4 アドレスのみで、IPv6はサポートされません。
- vmIdleTimeout=-1：WSLのアイドルタイムアウトを無効化する設定です。これにより、一定時間操作がない場合でもWSLが自動的に停止しないようになります。

保存後、ホストでWSLを再起動します。

```powershell
wsl --shutdown
```

さらに、Windows起動時にWSLを自動起動する設定を行います。

- `Win + R` + `taskschd.msc` でタスクスケジューラを開く
- 右側のペインで「タスクの作成」をクリック
- 「全般」タブ：
  - 名前：「Start WSL on Login」など
  - セキュリティオプション：「ユーザーがログオンしたときに実行する」を選択
  - 最上位の特権で実行するにチェック
- 「トリガー」タブ：
  - 「新規」をクリック
  - タスクの開始：「ログオン時」
  - 設定：「特定のユーザー」にチェックを入れ、ユーザーを選択
  - 遅延時間：30秒~1分程度（安定化のため）
  - 有効：チェック
- 「操作」タブ：
  - 「新規」をクリック
  - 操作：「プログラムの開始」
  - プログラム/スクリプト：`wsl.exe`
  - 引数の追加：`-d Ubuntu --exec dbus-launch true`
  - 開始：空欄

これで、Windows起動時に`wsl -d Ubuntu --exec dbus-launch true`コマンドが実行され、WSLが自動的に起動されるようになります。

### WSLの設定

`/etc/wsl.conf` に以下を追加します。これでWSL起動時にsshdが自動起動されます。

```ini
[boot]
systemd=true
```

さらに、以下のコマンドでSSHサーバを自動起動するようにします。

```bash
sudo systemctl enable ssh
```

ホストでWSLを再起動します。

```powershell
wsl --shutdown
```

これら一連の設定により、

- 安定してWSLが起動するようになり、
  - Windows起動時にWSLが自動的に起動される
  - WSL内でsystemdが有効化され、SSHサーバが自動起動される
  - 一定時間操作がない場合でもWSLが自動的に停止しない
- クライアントからホストWindowsのWSLへ安定してSSH接続できるようになります
  - WSLとホストWindowsのIPアドレスが一致（WSL起動ごとのIPアドレス変動を防ぐ）
  - ProxyJumpの際にwslのIPアドレスを127.0.0.1で指定できるようになる

### ProxyJumpの設定方法

クライアント側の`~/.ssh/config`に以下の設定を行います。

注意：remote-wslのHostNameは`localhost`**ではなく**`127.0.0.1`を指定します。`localhost`を指定すると、環境によってはIPv6で接続され接続に失敗する可能性があるためです。`127.0.0.1`を指定することで、明示的にIPv4経由で接続されるようになります。

```bash
Host remote-win
  HostName <hostname>  # or <hostname>.local or <ip-address>
  User windowsuser

Host remote-wsl
  HostName 127.0.0.1 # 明示的にIPv4を指定
  User wsluser
  Port 22222
  ProxyJump remote-win
```

これにより、クライアントから以下のコマンドで簡単にSSH接続できるようになります。

```bash
ssh remote-wsl
```

### （オプション）ミラーモードを用いない場合のWSL IPアドレスの更新

もしミラーモードを使用せず、WSLがホストとは別のIPアドレスを持つ場合、注意が必要です。

WSLは仮想NIC上で動作し、起動するたびにIPが変わるため、クライアント側の`~/.ssh/config`の`HostName`も更新する必要があります。

クライアント側で更新スクリプトを作成しておくと便利です。

まず、プロファイルのパスを確認します。

```powershell
$PROFILE
```

通常は `C:\Users\kouki\Documents\PowerShell\Microsoft.PowerShell_profile.ps1` のようなパスになります。

もしファイルが存在しない場合は、以下のコマンドで作成します。

```powershell
if (-not (Test-Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}
```

次に、VSCode等でプロファイルを開き、

```powershell
code $PROFILE
```

開いたファイルの末尾に以下の関数を追加します。

```powershell
function Update-WslIp {
    [CmdletBinding()]
    param(
        [string]$JumpHost = 'winusername@hostname',  # Jumphostのユーザー名とホスト名
        [string]$ConfigPath = "$HOME\.ssh\config",
        [string]$TargetHost = 'remote-wsl'
    )

    Write-Host "Fetching WSL IP via $JumpHost..." -ForegroundColor Cyan
    $wslIp = (ssh $JumpHost 'wsl hostname -I' 2>$null).Trim().Split(' ')[0]

    if (-not $wslIp) {
        Write-Error "Failed to get WSL IP address"
        return
    }

    if (-not (Test-Path $ConfigPath)) {
        Write-Error "$ConfigPath not found"
        return
    }

    # Get current IP (early return if no change is needed)
    $content = Get-Content $ConfigPath -Raw
    $pattern = "(?ms)(Host\s+$TargetHost\s*\r?\n(?:[^\r\n]*\r?\n)*?\s*HostName\s+)(\S+)"
    $currentMatch = [regex]::Match($content, $pattern)
    $currentIp = if ($currentMatch.Success) { $currentMatch.Groups[2].Value } else { $null }

    if ($currentIp -eq $wslIp) {
        Write-Host "IP is already up to date: $wslIp" -ForegroundColor Green
        return
    }

    # Back up and replace
    Copy-Item $ConfigPath "$ConfigPath.bak" -Force
    $updated = $content -replace $pattern, "`${1}$wslIp"
    Set-Content -Path $ConfigPath -Value $updated -NoNewline

    Write-Host "Updated: $currentIp -> $wslIp" -ForegroundColor Green
}

# Short alias (optional)
Set-Alias uwsl Update-WslIp
```

PowerShellを再起動するか、プロファイルを再読み込みします。

```powershell
. $PROFILE
```

以下のコマンドで使用できます。

```powershell
# エイリアス
uwsl

# フルコマンド
Update-WslIp -JumpHost 'windowsuser@hostname' -TargetHost 'remote-wsl'
```

## Windowsの設定（ポートフォワーディングを用いる場合）

JumpHostを用いることが出来ない環境の場合、Windowsのportproxy機能を用いて、リモートWindowsの特定のポート（例：22222）への接続をWSLのSSHサーバへ転送する方法もあります。

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

### クライアントからリモートのWSLへSSH接続

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

### トラブルシューティング

段階的に切り分けると原因が見つけやすいです：

- リモートWSL：`ss -tlnp | grep 22222` でsshdが22222で待ち受けているか確認
- リモートWindows：`netsh interface portproxy show v4tov4` で転送設定を確認
- リモートWindows：`ssh -p 22222 wsluser@localhost` でWSLへのローカル経由の接続を試す
- クライアント：`ssh username@hostname` でリモートWindowsへのSSH接続を試す
- クライアント：`ssh -4 -v -p 22222 wsluser@<WindowsのIP>` で外部経由を試す (`-v`で詳細なログを表示)

### WSLのIPアドレス自動更新

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

#### 方法1：Windowsログオン時にタスクスケジューラで自動実行

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

#### 方法2：WSL再起動後に手動実行

`wsl --shutdown` などでWSLを再起動した直後は、IPが変わっている可能性があります。その場合は、管理者権限のPowerShellで手動実行します。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File C:\Scripts\update-wsl-portproxy.ps1
```

実行後、`netsh interface portproxy show v4tov4` で転送先IPが最新のWSL IPに更新されていれば成功です。
