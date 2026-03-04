---
title: "Gitオプション: --force vs --force-with-lease"
description: ""
date: 2026-03-05T07:30:00+09:00
lastmod:
draft: false
---

## Gitオプション: --force vs --force-with-lease

Gitでリモートリポジトリに変更をpushする際、既存のcommitを上書きする必要がある場面があります。Gitにはこの目的のために`--force`と`--force-with-lease`という2つのオプションが用意されています。意図しない結果を避けるために、これらのオプションの違いを理解することが重要です。

| Feature                    | `--force`（または`-f`）                                | `--force-with-lease`                         |
| -------------------------- | ------------------------------------------------------ | -------------------------------------------- |
| **リモートcommitの上書き** | 無条件に上書き                                         | 安全に上書き                                 |
| **リモート状態の確認**     | なし                                                   | 上書き前にリモートが変更されていないか検証   |
| **データ損失のリスク**     | 高 - 他者の作業が失われる可能性あり                    | 低 - 他者のcommitの上書きを防止              |
| **ユースケース**           | 自分がリポジトリを管理している場合の強制push           | 共同作業の場合                               |
| **コマンド**               | `git push --force`                                     | `git push --force-with-lease`                |
| **検証の要否**             | 手動での確認が必要                                     | 自動安全チェック                             |
| **ベストプラクティス**     | 使用しない。使用する場合、特に共同作業時は注意して使用 | 全ての場合。特にチーム環境での推奨           |
| **失敗した場合**           | 失敗なし、常にpushが成功                               | リモートに新しいcommitがある場合はpushが失敗 |

個人branchで作業している場合でも、習慣にするために`--force-with-lease`を使うことをお勧めします。

### それぞれの使い分け

**`--force`を使う場合:**

- 個人branchで作業している場合
- 他の誰もそのbranchにpushしていないことを確認した場合
- pushに対する完全な制御が必要な場合

**`--force-with-lease`を使う場合:**

- チーム環境での作業
- 他者の変更を誤って上書きすることへの保護が必要な場合
- より安全な強制pushオプションが必要な場合

## `--force-with-lease`が失敗するシナリオ例

- **Person Aのローカルbranch:** commit`abc123`の`feature/new-feature`
- **リモートbranch:** commit`abc123`の`feature/new-feature`
- **Person BがPush:** リモートの`feature/new-feature`に新しいcommit`def456`
- **Person Aが試みる:** `git push --force-with-lease`

**結果:** ❌ Pushがエラーで失敗:

```bash
error: failed to push some refs to 'origin'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you are integrating with upstream changes
hint: you may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

Person Aの`--force-with-lease`は、最後のfetch以降にリモートが変更されたことを検知し、Person Bのcommit`def456`の上書きを安全に防止します。
