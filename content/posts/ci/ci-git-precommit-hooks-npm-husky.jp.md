---
title: "npmとhuskyを使ったGit pre-commitフックによるCI"
description: ""
date: 2026-03-04T8:00:00+09:00
lastmod:
math: false
draft: false
---

## npmとhuskyを使ったGit pre-commitフックによるCI

- [Git pre-commitフック](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)を使うと、コミット前にスクリプトを実行できます。これはテスト、リンター、その他のチェックを実行してコード品質を確保するのに役立ちます。[npm husky](https://typicode.github.io/husky/#/)は、JavaScriptプロジェクトでGitフックを簡単に管理できる人気のツールです。

## fnm経由でnpmをインストール

詳細は[fnm - Fast and simple Node.js version manager](https://github.com/Schniz/fnm)を参照してください。

```bash
sudo apt install -y curl unzip

curl -fsSL https://fnm.vercel.app/install | bash

fnm --version
```

最新の安定版Node.jsをインストール：

```bash
# 最新の安定版Node.jsをインストール
fnm install --lts


# 使用する（現在のシェルセッションのみ）
fnm use --lts

# デフォルトに設定（すべてのシェルセッションのデフォルト）
fnm default lts-latest

# 確認
node --version
npm --version
```

## プロジェクトのセットアップ

```bash
cd your-project

# npmプロジェクトを初期化
npm init -y

# huskyをインストール
npm install husky --save-dev

# huskyを初期化（.husky/pre-commitを作成し、prepareスクリプトを追加）
npx husky init

# .husky/pre-commitを編集してフックコマンドを追加
echo "npm test" >> .husky/pre-commit
```

また、`package.json`にテストスクリプトを手動で追加します：

```json
"scripts": {
  "prepare": "husky",
  "test": "echo \"Running tests...\" && exit 0"
}
```

これで、変更をコミットしようとするたびに、pre-commitフックがコミットを許可する前に`npm test`を実行します。`npm test`は、pre-commitチェックとして実行したい任意のコマンドに置き換えることができます。
