---
title: "仕様駆動AIコーディングのための Spec Kitプロジェクト準備"
description: ""
date: 2025-12-14T10:00:00+09:00
lastmod:
math: true
draft: false
---

## 仕様駆動AIコーディングのためのSpec Kitプロジェクト準備

Spec Kitで仕様駆動AIコーディングを使用するには、Spec Kitプロジェクトをセットアップする必要があります。以下の手順に従って、プロジェクト環境を準備してください。

新しいプロジェクトを作成:

```bash
# プロジェクトディレクトリを作成
mkdir your-project
cd your-project
```

Python仮想環境を作成:

```bash
# 仮想環境を作成して有効化
python -m venv venv
source venv/bin/activate
```

[uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)をインストール:

```bash
# pipをアップデートしてuvをインストール
pip install -U pip
pip install uv
```

uvを使用して[Spec Kit](https://github.com/github/spec-kit)をインストール:

```bash
# Spec Kitをインストール
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

(オプション)シェル設定を更新:

```bash
# シェル設定を更新して再読み込み
uv tool update-shell
source ~/.bashrc
source venv/bin/activate
```

Spec Kitプロジェクトを初期化:

```bash
# 現在のディレクトリでSpec Kitを初期化
specify init --here
```
