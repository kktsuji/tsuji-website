---
title: "リモートWindowsへSSH接続"
description: ""
date: 2026-05-23T16:00:00+09:00
lastmod:
draft: false
---

## Pingの確認

まず、クライアントからリモートWindowsのIPアドレスに対してPingを送信して、ネットワーク接続が確立されているか確認します。

リモートのPC名が<hostname>のとき：

```powershell
# Windows同士の場合
ping <hostname>

# mDNSを使う場合（macOS/Linux/WSLなど）
ping <hostname>.local
```

リモートのIPアドレスでも確認できます：

```powershell
# リモートで `ipconfig` でIPアドレスを確認した後
ping <ip-address>
```

### `.local`の有無による使い分け

`.local` はmDNS（Multicast DNS、RFC 6762）で使われる特別なドメインで、LAN内でDNSサーバーを介さずに名前解決ができます。クライアントの環境によって使い分けます。

`ping <hostname>`（`.local`なし）を使う場面：

- クライアントがWindowsで、リモートもWindows（同じLAN内）
  - NetBIOS over TCP/IPまたはLLMNRで解決される
- 社内DNSサーバーにPC名が登録されている環境（ドメイン参加PCなど）
- DNSサフィックス（例：`corp.example.com`）が設定済みで、`<hostname>` だけでFQDNに補完される

`ping <hostname>.local` を使う場面：

- クライアントが macOS / Linux / iOS / Android からWindowsを探す
  - Bonjour (macOS) / Avahi (Linux) が mDNSで解決
- DNSサーバーが無い家庭LAN / 小規模オフィス
- NetBIOS / LLMNRが無効化されているセキュリティ強化環境
- IoT / Raspberry PiなどmDNSが標準の機器と混在

早見表：

| クライアント → リモート           | 推奨                                      |
| --------------------------------- | ----------------------------------------- |
| Windows → Windows（家庭LAN）      | どちらでも可。まず`.local`なし            |
| Windows → Windows（社内ドメイン） | `.local`なし                              |
| macOS / Linux → Windows           | `.local`あり                              |
| WSL → ホストWindows               | `.local`あり（または`$(hostname).local`） |

なお、Windows側で`.local`を使うにはBonjour Print ServicesまたはWindows 10 1803以降の組み込みmDNSが必要です。古いWindowsだと`.local`が効かないケースもあります。

## Pingが通らない場合

### ファイアウォールの確認

リモートでWindowsのファイアウォールがICMP（Ping）をブロックしている可能性があります。以下の手順で確認します。

1. リモートWindowsで「セキュリティが強化されたWindows Defenderファイアウォール」を開く。
2. 左側の「受信の規則」をクリック。
3. 「ファイルとプリンターの共有（エコー要求 - ICMPv4-In）」を探す。
4. 状態が「有効」かつ「許可」になっていることを確認。
5. もし無効やブロックされている場合は、右クリックして「規則の有効化」を選択。
6. 同様に「ファイルとプリンターの共有（エコー要求 - ICMPv6-In）」も確認（IPv6環境の場合）。

### ルーターの確認

家庭やオフィスのルーターがICMPをブロックしている可能性もあります。ルーターの管理画面にアクセスして、ファイアウォール設定やセキュリティ設定を確認してください。特に「Ping応答を許可する」などのオプションがある場合は有効にします。

### ウイルス対策ソフトの確認

一部のウイルス対策ソフトやセキュリティソフトがICMPをブロックすることがあります。リモートWindowsにインストールされているセキュリティソフトの設定を確認し、必要に応じてICMPを許可してください。

## SSHサーバの設定

Pingが通ることを確認したら、リモート側でSSHサーバを設定します。Windows 10以降では、OpenSSHサーバが組み込まれているため、以下の手順で有効化できます。

1. 「設定」→「アプリ」→「オプション機能」を開く。
2. 「機能の追加」をクリック。
3. 「OpenSSHサーバ」を検索して選択し、「インストール」をクリック。

もしくはPowerShellを管理者権限で開いて、以下のコマンドを実行してインストールします。

```powershell
# OpenSSHサーバのインストール状況の確認
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Server*'
```

結果の判定：

- `State : Installed` と表示された場合：インストール済み。そのまま設定進む。
- `State : NotPresent` と表示された場合：未インストール。

インストールする場合：

```powershell
Add-WindowsCapability -Online -Name "OpenSSH.Server~~~~0.0.1.0"
```

インストール完了後、以下の設定を行います。

```powershell
# サービスを自動起動に設定
Set-Service -Name sshd -StartupType 'Automatic'

# 今すぐサービスを開始
Start-Service sshd

# ステータス確認
Get-Service -Name sshd
```

ステータス確認で `Status: Running` になっていれば、リモートPC側でのSSHサーバーの立ち上げは完了です。

## クライアントからSSH接続

クライアントからリモートWindowsにSSH接続するには、以下のコマンドを使用します。

```bash
ssh <username>@<hostname>  # または <username>@<hostname>.local
```

ユーザー名はリモートWindowsのアカウント名を指定します。接続が成功すると、リモートWindowsのコマンドプロンプトやPowerShellにアクセスできます。

ただし、初回接続時にはホストキーの確認が求められるため、表示される指紋を確認してから「yes」と入力してください。

また、この状態では毎回の接続でパスワードを入力する必要があります。パスワードなしで接続したい場合は、SSHキーを生成してリモートWindowsに公開鍵を配置します。

以下、クライアント側でSSHキーを生成する例です。

```powershell
# クライアント側でSSHキーを生成
ssh-keygen -t ed25519
```

これにより、`~/.ssh/id_ed25519`（秘密鍵）と`~/.ssh/id_ed25519.pub`（公開鍵）が生成されます。公開鍵の内容をリモートWindowsのユーザープロファイルの`.ssh/authorized_keys`に追加することで、パスワードなしでSSH接続が可能になります。

```powershell
# 公開鍵をリモートWindowsにコピー
type ~/.ssh/id_ed25519.pub | ssh <username>@<hostname> "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

もしくは以下のコマンドで直接コピーすることもできます。

```powershell
# リモートへssh接続
ssh <username>@<hostname>

# リモート側に「.ssh」フォルダ作成
New-Item -ItemType Directory -Path "$HOME\.ssh" -Force

# ローカルの公開鍵をリモートのauthorized_keysに貼り付け
Set-Content -Path "$HOME\.ssh\authorized_keys" -Value "ここにコピーした公開鍵を貼り付け"
```

最後に、リモート側で公開鍵の権限を適切に設定します。

```powershell
# 公開鍵の権限を設定（WindowsのACLで管理者とユーザーにフルコントロールを付与）
icacls "$HOME\.ssh\authorized_keys" /inheritance:r /grant:r "Administrators:F" /grant:r "${env:USERNAME}:F"
```

### リモートへ管理者としてSSH接続する場合

リモートのアカウント設定によっては、SSH接続後に自動で管理者権限になることがあります。

その場合、公開鍵は管理者アカウントのホームディレクトリの`.ssh/authorized_keys`に配置する必要があります。

```powershell
# システム共通の公開鍵保存フォルダを作成
New-Item -ItemType Directory -Path "$env:ProgramData\ssh" -Force

# 管理者用の公開鍵ファイルにコピーした公開鍵を貼り付け
Set-Content -Path "$env:ProgramData\ssh\administrators_authorized_keys" -Value "ここにコピーした公開鍵を貼り付け"

# 公開鍵の権限を設定（管理者とSYSTEMにフルコントロールを付与）
icacls "$env:ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant:r "Administrators:F" /grant:r "SYSTEM:F"
```

## クライアントのSSH設定

クライアント側でSSH接続を簡略化するために、`~/.ssh/config`ファイルにリモートWindowsの設定を追加することができます。

```bash
Host remote-win
  HostName <hostname>  # または <hostname>.local or <ip-address>
  User <username>
```

これにより、以下のコマンドで簡単にSSH接続できるようになります。

```bash
# ssh <username>@<hostname> の代わりに以下で接続可能
ssh remote-win
```
