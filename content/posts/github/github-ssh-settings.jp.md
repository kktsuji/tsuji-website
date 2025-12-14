---
title: "GitHubへの安全なアクセスのためのSSH設定"
description: ""
date: 2025-10-19T11:00:00+09:00
lastmod:
draft: false
---

参照：[Connecting to GitHub with SSH - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

## GitHubのSSHキーのセットアップ

環境：Ubuntu 22.04 LTS

### 1. 既存のSSHキーを確認

```bash
ls -al ~/.ssh
```

`id_rsa`と`id_rsa.pub`のようなファイルが表示される場合、すでにSSHキーが存在します。表示されない場合は、次のステップに進みます。

### 2. 新しいSSHキーペアを生成

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

以下のような対話的なプロンプトには、何も入力せずにEnterキーを押すだけでよいです：

```bash
Enter file in which to save the key:
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

### 3. 公開鍵をクリップボードにコピー

```bash
cat ~/.ssh/id_ed25519.pub
```

### 4. SSHキーをGitHubアカウントに追加

1. Github > Settings > SSH and GPG keys > New SSH keyに移動
2. コピーした公開鍵を「Key」フィールドに貼り付け、タイトルを付けます。

### 5. SSH接続をテスト

```bash
ssh -T git@github.com
```

以下のようなメッセージが表示されるはずです：

```plaintext
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```
