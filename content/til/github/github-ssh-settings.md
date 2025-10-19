---
title: 'GitHub SSH Settings for Secure Access'
description: ''
date: 2025-10-19T11:00:00+09:00
lastmod: 
draft: false
---

## Setting Up SSH Keys for GitHub

Environment: Ubuntu 22.04 LTS

### 1. Check for existing SSH keys

```bash
ls -al ~/.ssh
```

If you see files like `id_rsa` and `id_rsa.pub`, you already have SSH keys. If not, proceed to the next step.

### 2. Generate a new SSH key pair

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

You can only enter without input something to the interactive prompts like below:

```bash
Enter file in which to save the key:
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

### 3. Copy the public key to your clipboard

```bash
cat ~/.ssh/id_ed25519.pub
```

### 4. Add the SSH key to your GitHub account

1. Go to Github > Settings > SSH and GPG keys > New SSH key
2. Paste the copied public key into the "Key" field and give it a title.

### 5. Test the SSH connection

```bash
ssh -T git@github.com
```

You should see a message like:

```plaintext
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```
