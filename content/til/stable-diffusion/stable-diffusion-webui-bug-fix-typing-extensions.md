---
title: 'Fix a Bug "typing-extensions" of stable-diffusion-webui'
description: ''
date: 2024-10-29T9:30:00+09:00
lastmod: 
draft: false
---

AbdBarho's [stable-diffusion-webui-docker](https://github.com/AbdBarho/stable-diffusion-webui-docker) has a bug when we use a command ``docker compose --profile auto up --build`` to build and run docker containers.

This's due to [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) of AUTOMATIC1111 (as of Oct. 29, 2024).

**Fix a bug:**

```bash
clone https://github.com/AbdBarho/stable-diffusion-webui-docker.git

cd stable-diffusion-webui-docker

vim ./services/AUTOMATIC1111/Dockerfile
```

Then modify following:

```bash
   git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git && \
   cd stable-diffusion-webui && \
   git reset --hard v1.9.4 && \
-  pip install -r requirements_versions.txt
+  pip install -r requirements_versions.txt && \
+  pip install --upgrade typing-extensions
```

Save it.

We can execute docker commands correctly:

```bash
docker compose --profile download up --build
docker compose --profile auto up --build
```

**Reference:**

- [[Bug]: ImportError: cannot import name 'TypeIs' from 'typing_extensions' #16520 - GitHub Issues](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/16520)
- [docker compose --profile auto-cpu up --build -> ImportError: cannot import name 'TypeIs' from 'typing_extensions' - exited with code 1- #742 - GitHub Issues](https://github.com/AbdBarho/stable-diffusion-webui-docker/issues/742)
