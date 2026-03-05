---
title: 'GitHubにおける2段階のbranch protection: pushできるユーザーの管理'
description: ""
date: 2026-03-05T08:00:00+09:00
lastmod:
draft: false
---

## GitHubにおける2段階のbranch protection: pushできるユーザーの管理

ownerとcollaboratorだけが直接pushできる（可能性のある）立場にありますが、コード品質とセキュリティを確保するために**ルールによって制限される**ことがほとんどです。pushしようとして「protected branch」というエラーが表示された場合、あなたの権限に関わらず、プロジェクトがPRを要求していることを意味します。

## 1. アクセスロール（"Permission"を持つのは誰か？）

リポジトリに何かをpushするには、まず**Write Access**が必要です。

- **Repository Owners:** デフォルトで完全な制御権を持ちます。
- **Collaborators:** "Write"または"Admin"権限が付与されている場合に限り、直接pushできます。

## 2. Branch Protection（なぜOwnerやCollaboratorでもブロックされる場合があるのか）

多くのプロジェクトでは、`main`または`develop`ブランチは通常「protected」になっています。

**Branch Protection Rules**が有効な場合：

- **直接pushは無効化されています:** ownerであっても、GitHubは直接pushを拒否します。
- **PRの必須化:** Pull Requestを作成し、自動テストを通過し、多くの場合はコードがマージされる前にピアレビューを受けることが求められます。

### まとめ

| シナリオ                 | 直接pushできるのは誰？ | 備考                                   |
| ------------------------ | ---------------------- | -------------------------------------- |
| **保護なし**             | Write accessを持つ全員 | 速いが、本番コードにはリスクがある。   |
| **Protected Branch**     | **誰も不可**（通常）   | 全員がPull Requestを使う必要がある。   |
| **例外付きのProtection** | AdminsやSpecific users | "Bypass"を許可するルールが設定できる。 |
