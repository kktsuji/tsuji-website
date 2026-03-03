---
title: "小規模OSSプロジェクトにおけるGitHub FlowのBranch Protection設定"
description: ""
date: 2026-03-03T09:00:00+09:00
lastmod:
draft: false
---

## 前提条件

- GitHub上のOSSリポジトリ
- リポジトリのAdmin権限
- GitHub Flowワークフローの使用
  - Defaultブランチは`main`
  - FeatureブランチはDefaultブランチから作成され、Pull requestを経てDefaultブランチにマージされる
  - Pull requestはコードレビュー、Continuous integration (CI) チェックに使用される

## 達成したいこと

- 誰もDefaultブランチに直接pushできない。すべての変更はPull requestを通じて行われなければならない
- Pull requestをマージする前にCIチェックがpassする必要がある
- CopilotがPull requestのレビューに自動追加され、コードレビューを支援してコード品質を維持する
- Pull requestをマージする前にすべての会話が解決されなければならない
- Pull requestは`Squash and merge`または`Rebase and merge`を使用してマージし、クリーンなコミット履歴を維持する
- Pull requestがマージされた後にブランチを自動的に削除し、リポジトリをクリーンで整理された状態に保つ

## GitHubリポジトリの設定

### General設定

GitHubリポジトリ > Settings > Generalに移動

- `Default branch`を`main`に設定する
- `Allow merge commits`を無効にして、Defaultブランチへのマージコミットを防ぎ、よりクリーンなコミット履歴を維持する
- `Allow squash merging`を有効にする。これはFeatureブランチのすべてのコミットを1つのコミットにまとめることで、よりクリーンなコミット履歴の維持に役立つ
  - `Allow squash merging`の`Pull request title and description`を設定する。これにより、マージされる変更のコンテキストが提供される
- `Allow rebase merging`を有効にする。これはFeatureブランチのコミットをDefaultブランチにマージする前にrebaseすることで、よりクリーンなコミット履歴の維持に役立つ
- `Allow auto-merge`を無効にして、CIチェックとコードレビューをpassせずにPull requestが自動的にマージされるのを防ぐ
- `Automatically delete head branches`を有効にして、Pull requestがマージされた後にFeatureブランチを自動的に削除し、リポジトリをクリーンで整理された状態に保つ

### Rules設定

GitHubリポジトリ > Settings > Rules > New rulesetに移動

- `<Ruleset name>`を`Ruleset name`に設定する
- `Active`を`Enforcement status`に設定する
- `Default branch`を`Target branches`に設定する
- `Require a pull request before merging`を有効にして、Defaultブランチへのすべての変更がPull requestを通じて行われるようにする。これにより、マージ前にコードレビューとCIチェックが可能になる
  - `Require conversation resolution before merging`を有効にする。これはコード品質の維持と、すべてのフィードバックが対応されることを確実にするのに役立つ
  - `Allowed merge methods`で`Merge`を無効にして`Squash`と`Rebase`を有効にする。これはマージコミットを防ぎ、squashとrebaseマージのみを許可することで、よりクリーンなコミット履歴の維持に役立つ
- `Require status checks to pass`を有効にして、Pull requestをマージする前にすべてのCIチェックがpassすることを確実にする。これはコード品質の維持と、壊れたコードがDefaultブランチにマージされるのを防ぐのに役立つ
  - 設定したCIアクションを`Status checks that are required`に追加する。これにより、設定した特定のCIチェックがPull requestのマージ前にpassすることが必須になる
- `Block force pushes`を有効にして、Defaultブランチへのforce pushを防ぐ。force pushはコミット履歴を上書きし、コラボレーターに問題を引き起こす可能性がある
- `Automatically request Copilot code review`を有効にして、コードレビューを支援しコード品質を維持する
