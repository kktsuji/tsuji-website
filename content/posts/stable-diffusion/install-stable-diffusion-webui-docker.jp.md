---
title: "stable-diffusion-webui-dockerをインストールする"
description: ""
date: 2024-11-21T9:00:00+09:00
lastmod:
draft: false
---

AbdBarhoの[stable-diffusion-webui-docker](https://github.com/AbdBarho/stable-diffusion-webui-docker)を使用すると、AUTOMATIC1111の[stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)をDockerコンテナ上で実行できます。

メリット：

- Windows PCの環境をクリーンに保てる（PCに直接gitやpythonをインストールする必要がない）

準備：

1. Nvidia GPUを搭載したWindows PCに適切な[NVIDIA Graphics Driver](https://www.nvidia.com/en-us/drivers/)をインストールします。
2. Windows PCにwsl2をインストールします（[Microsoftの公式ドキュメント](https://learn.microsoft.com/en-us/windows/wsl/install)を参照）。
3. WSLディストリビューションに[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)をインストールします。
4. Windows PCに[Docker Desktop](https://www.docker.com/products/docker-desktop/)をインストールします（WSL統合を有効化）。

WSLでコマンドを実行：

```bash
git clone https://github.com/AbdBarho/stable-diffusion-webui-docker.git

cd stable-diffusion-webui-docker

docker compose --profile download up --build

docker compose --profile auto up --build
```

その後、Webブラウザで`http://localhost:7860/`にアクセスします。
