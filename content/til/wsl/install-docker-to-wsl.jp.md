---
title: "WSLへのDockerのインストール"
description: ""
date: 2025-03-26T08:00:00+09:00
lastmod:
draft: false
---

## 前提条件

- WindowsにWSL2とUbuntu 22.04をインストール（[以前の投稿](https://tsuji.tech/install-uninstall-wsl/)を参照）

## WSLへのDockerのインストール

WSLにDockerをインストール（[Install Docker Engine on Ubuntu - Docker Docs](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)を参照）：

```bash
# Dockerの公式GPGキーを追加：
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# リポジトリをAptソースに追加：
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

dockerコマンドが有効であることを確認：

```bash
sudo docker run hello-world
```

## root以外のユーザーとしてDockerを管理

dockerグループが存在することを確認（[Linux post-installation steps for Docker Engine - Docker Docs](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)を参照）：

```bash
grep docker /etc/group

# dockerグループが存在する場合、以下のレスポンスが表示される：
# docker:x:999:

# 存在しない場合、dockerグループを追加：
sudo groupadd docker
```

自分のユーザーをdockerグループに追加：

```bash
sudo usermod -aG docker $USER
```

PowerShellでWSLを再起動（WSL上ではなく）：

```bash
wsl --shutdown
```

WSL上でdockerグループを有効化：

```bash
newgrp docker
```

次に、sudoなしでdockerコマンドを実行できることを確認：

```bash
docker run hello-world
```

## 参考文献

- [Install Docker Engine on Ubuntu - Docker Docs](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- [Linux post-installation steps for Docker Engine - Docker Docs](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
