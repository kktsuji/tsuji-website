---
title: "Git LFSのセットアップ"
description: ""
date: 2026-02-19T18:00:00+09:00
lastmod:
draft: false
---

## Git LFS (Large File Storage) のセットアップ

```bash
# Git LFSをインストール
sudo apt-get update
sudo apt-get install git-lfs -y

# 現在のユーザーにGit LFSを設定
# このコマンドはユーザーごとに一度だけ実行する
git lfs install
```

## 使用例

Gitリポジトリに大きなファイルをコミットする場合：

```bash
cd <your-git-repository>

# 特定のファイルを追跡（例：.psdファイル）
# 最初にこのコマンドを実行する
# Git LFSが追跡するファイルを記録する.gitattributesファイルを作成or変更するため
git lfs track "*.psd"

# .gitattributesファイルをadd
# 大きなファイルを追加する前にトラッキング設定が整っていることを確認するため、コミットを分けるとベター
git add .gitattributes
git commit -m "Track .psd files with Git LFS"

# 通常通り大きなファイルを追加してコミット
git add path/to/your/largefile.psd
git commit -m "Add large file with Git LFS"

# リモートリポジトリにプッシュ
git push origin main
```

Git LFSを使用するリポジトリをクローンする場合：

```bash
git clone <repository-url>

cd <repository-directory>

 # Git LFSで追跡されている大きなファイルをダウンロード
git lfs pull
```
