---
title: 'Install stable-diffusion-webui-docker'
description: ''
date: 2024-11-21T9:00:00+09:00
lastmod: 
draft: false
---

AbdBarho's [stable-diffusion-webui-docker](https://github.com/AbdBarho/stable-diffusion-webui-docker) can execute AUTOMATIC1111's [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) on a docker container.

Merits:

- Keep my Windows PC environment clean (no need to install git or python directly on my PC)

Preparation:

1. Install the appropriate [NVIDIA Graphics Driver](https://www.nvidia.com/en-us/drivers/) on a Windows PC with a Nvidia GPU.
2. Install wsl2 on the Windows PC (see [Microsoft's official document](https://learn.microsoft.com/en-us/windows/wsl/install)).
3. Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) on a WSL distribution.
4. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) on the Windows PC (Enable WSL integration).

Execute commands in WSL:

```bash
git clone https://github.com/AbdBarho/stable-diffusion-webui-docker.git

cd stable-diffusion-webui-docker

docker compose --profile download up --build

docker compose --profile auto up --build
```

Then access ``http://localhost:7860/`` in a web browser.
