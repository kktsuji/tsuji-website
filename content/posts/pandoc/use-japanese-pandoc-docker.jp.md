---
title: "Pandoc Dockerイメージで日本語を使用する"
description: ""
date: 2025-04-09T07:00:00+09:00
lastmod:
draft: false
---

## Pandoc Dockerイメージで日本語を使用する

[pandoc/latex](https://hub.docker.com/r/pandoc/latex) Dockerイメージはデフォルトでは日本語をサポートしていません。日本語を使用するには、`collection-langjapanese`パッケージをインストールする必要があります。

次の内容で`Dockerfile`を作成します：

```dockerfile
FROM pandoc/latex:3.6.4.0-ubuntu
RUN apt-get update && \
    apt-get upgrade -y && \
    tlmgr update --self --all && \
    tlmgr install collection-langjapanese
```

`tlmgr`はTeX Liveパッケージマネージャーです。上記のコマンドは、パッケージリストを更新し、すべてのパッケージをアップグレードし、`collection-langjapanese`パッケージをインストールします。

次に、Dockerイメージをビルドします。

```bash
docker build -t pandoc/japanese .
```

これで、`pandoc/japanese`イメージを使用して日本語サポート付きのドキュメントを変換できます。

```bash
docker run --rm \
    --volume "$(pwd):/data" \
    --user $(id -u):$(id -g) \
    pandoc/japanese doc.md -o doc.pdf \
    --pdf-engine=lualatex -V documentclass=ltjsarticle
```

## 参考文献

- [pandoc/latex - Docker Hub](https://hub.docker.com/r/pandoc/latex)
- [楽にDockerで日本語Pandocする - Qiita](https://qiita.com/kojix2/items/1d2db46858ce202628d2)
- [メモ: Pandoc+LaTeXで気軽に日本語PDFを出力する - Qiita](https://qiita.com/sky_y/items/15bf7737f4b37da50372)
