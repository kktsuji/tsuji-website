---
title: 'stable-diffusion-webuiの"typing-extensions"バグを修正'
description: ""
date: 2024-10-29T9:30:00+09:00
lastmod:
draft: false
---

AbdBarhoの[stable-diffusion-webui-docker](https://github.com/AbdBarho/stable-diffusion-webui-docker)には、`docker compose --profile auto up --build`コマンドを使用してDockerコンテナをビルドおよび実行する際にバグがあります。

これはAUTOMATIC1111の[stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)に起因するものです（2024年10月29日時点）。

**バグの修正：**

```bash
clone https://github.com/AbdBarho/stable-diffusion-webui-docker.git

cd stable-diffusion-webui-docker

vim ./services/AUTOMATIC1111/Dockerfile
```

次のように修正します：

```bash
   git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git && \
   cd stable-diffusion-webui && \
   git reset --hard v1.9.4 && \
-  pip install -r requirements_versions.txt
+  pip install -r requirements_versions.txt && \
+  pip install --upgrade typing-extensions
```

保存します。

これでDockerコマンドを正しく実行できます：

```bash
docker compose --profile download up --build
docker compose --profile auto up --build
```

**参考文献：**

- [[Bug]: ImportError: cannot import name 'TypeIs' from 'typing_extensions' #16520 - GitHub Issues](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/16520)
- [docker compose --profile auto-cpu up --build -> ImportError: cannot import name 'TypeIs' from 'typing_extensions' - exited with code 1- #742 - GitHub Issues](https://github.com/AbdBarho/stable-diffusion-webui-docker/issues/742)
