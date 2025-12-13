---
title: "Use NVIDIA GPU with WSL Docker"
description: ""
date: 2025-03-28T22:00:00+09:00
lastmod:
draft: false
---

## Prerequisites

1. Install WSL2 and Ubuntu 22.04 to Windows (see [my previous post](https://tsuji.tech/install-uninstall-wsl/))
2. Install Docker to WSL (see [my previous post](https://tsuji.tech/install-docker-to-wsl/))

## Install NVIDIA Driver to Windows

Install NVIDIA driver to Windows (see [NVIDIA Driver Downloads](https://www.nvidia.com/en-us/drivers/)):

## Install NVIDIA Container Toolkit to WSL

Install NVIDIA Container Toolkit to WSL (see [Installing the NVIDIA Container Toolkit - NVIDIA](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)):

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# Restart docker
sudo systemctl restart docker
```

Configure docker:

```bash
sudo nvidia-ctk runtime configure --runtime=docker

# Restart docker
sudo systemctl restart docker
```

## Test NVIDIA GPU with Docker

Test NVIDIA GPU with Docker with cuda image (see [nvidia/cuda - Dockerhub](https://hub.docker.com/r/nvidia/cuda)):

```bash
docker run --rm --gpus all nvidia/cuda:12.8.0-cudnn-runtime-ubuntu22.04 nvidia-smi
```
