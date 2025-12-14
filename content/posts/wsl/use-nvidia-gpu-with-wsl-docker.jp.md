---
title: "WSL DockerでNVIDIA GPUを使用"
description: ""
date: 2025-03-28T22:00:00+09:00
lastmod:
draft: false
---

## 前提条件

1. WindowsにWSL2とUbuntu 22.04をインストール（[以前の投稿](https://tsuji.tech/install-uninstall-wsl/)を参照）
2. WSLにDockerをインストール（[以前の投稿](https://tsuji.tech/install-docker-to-wsl/)を参照）

## WindowsにNVIDIAドライバをインストール

WindowsにNVIDIAドライバをインストール（[NVIDIA Driver Downloads](https://www.nvidia.com/en-us/drivers/)を参照）：

## WSLにNVIDIA Container Toolkitをインストール

WSLにNVIDIA Container Toolkitをインストール（[Installing the NVIDIA Container Toolkit - NVIDIA](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)を参照）：

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# Dockerを再起動
sudo systemctl restart docker
```

Dockerを設定：

```bash
sudo nvidia-ctk runtime configure --runtime=docker

# Dockerを再起動
sudo systemctl restart docker
```

## DockerでNVIDIA GPUをテスト

cudaイメージを使用してDockerでNVIDIA GPUをテスト（[nvidia/cuda - Dockerhub](https://hub.docker.com/r/nvidia/cuda)を参照）：

```bash
docker run --rm --gpus all nvidia/cuda:12.8.0-cudnn-runtime-ubuntu22.04 nvidia-smi
```
