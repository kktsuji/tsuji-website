---
title: "Use Japanese in Pandoc Docker Image"
description: ""
date: 2025-04-09T07:00:00+09:00
lastmod:
draft: false
---

## Use Japanese in Pandoc Docker Image

[pandoc/latex](https://hub.docker.com/r/pandoc/latex) Docker image does not support Japanese by default. To use Japanese, `collection-langjapanese` package must be installed.

Create a `Dockerfile` with the following content:

```dockerfile
FROM pandoc/latex:3.6.4.0-ubuntu
RUN apt-get update && \
    apt-get upgrade -y && \
    tlmgr update --self --all && \
    tlmgr install collection-langjapanese
```

`tlmgr` is a TeX Live package manager. The above command updates the package list, upgrades all packages, and installs the `collection-langjapanese` package.

Then, build the Docker image.

```bash
docker build -t pandoc/japanese .
```

You can now use the `pandoc/japanese` image to convert documents with Japanese support.

```bash
docker run --rm \
    --volume "$(pwd):/data" \
    --user $(id -u):$(id -g) \
    pandoc/japanese doc.md -o doc.pdf \
    --pdf-engine=lualatex -V documentclass=ltjsarticle
```

## References

- [pandoc/latex - Docker Hub](https://hub.docker.com/r/pandoc/latex)
- [楽にDockerで日本語Pandocする - Qiita](https://qiita.com/kojix2/items/1d2db46858ce202628d2)
- [メモ: Pandoc+LaTeXで気軽に日本語PDFを出力する - Qiita](https://qiita.com/sky_y/items/15bf7737f4b37da50372)
