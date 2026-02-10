---
title: "一般的なソフトウェアアーキテクチャの種類"
description: ""
date: 2026-02-10T18:00:00+09:00
lastmod:
draft: false
---

## 一般的なソフトウェアアーキテクチャの種類

### 1. Layered (N-Tier)

**構造:** 水平レイヤー(Presentation → Business → Data Access → Database)

- ✅ シンプル、馴染みやすい、関心の分離
- ❌ レイヤー間の密結合、変更が下位レイヤーに波及する

```
src/
├── presentation/    # Controllers、Views
├── business/        # Services、Business Logic
├── dataaccess/      # Repositories、DAOs
└── models/          # 共有DTOs、Entities
```

### 2. Hexagonal (Ports & Adapters)

**構造:** コアドメインをports（インターフェース）とadapters（実装）が取り囲む

- ✅ 高いテスタビリティ、ドメイン中心、インフラストラクチャの交換可能性
- ❌ セットアップが複雑、シンプルなアプリには過剰

```
src/
├── domain/          # コアビジネスロジック
│   ├── models/
│   └── services/
├── ports/           # インターフェース（入出力）
│   ├── inbound/
│   └── outbound/
└── adapters/        # 実装
    ├── web/         # RESTコントローラー
    └── persistence/ # データベースアダプター
```

### 3. Vertical Slice

**構造:** すべてのレイヤーを横断する独立したスライスとして機能を編成

- ✅ 機能間の低結合、単一機能の理解が容易
- ❌ コードの重複の可能性、一貫性の維持が困難

```
src/
├── features/
│   ├── create-order/
│   │   ├── handler.ts
│   │   ├── validator.ts
│   │   └── repository.ts
│   ├── get-order/
│   │   ├── handler.ts
│   │   └── repository.ts
│   └── cancel-order/
└── shared/          # 横断的関心事
```

### 4. Clean Architecture

**構造:** 同心円 (Entities → Use Cases → Interface Adapters → Frameworks)

- ✅ フレームワーク非依存、高いテスタビリティ、柔軟性
- ❌ 学習曲線が急、多くのボイラープレート

```
src/
├── entities/        # エンタープライズビジネスルール
├── usecases/        # アプリケーションビジネスルール
├── interfaces/      # アダプター（controllers、gateways）
│   ├── controllers/
│   └── gateways/
└── frameworks/      # 外部ツール(DB、Web)
    ├── database/
    └── web/
```

### 5. Microservices

**構造:** API経由で通信する独立したデプロイ可能なサービス

- ✅ 独立したスケーリング/デプロイ、技術の柔軟性、障害の分離
- ❌ ネットワークの複雑さ、分散システムの課題、運用オーバーヘッド

```
services/
├── user-service/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── order-service/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── payment-service/
└── api-gateway/
```

### 6. Monolithic

**構造:** すべての機能を含む単一デプロイ可能ユニット

- ✅ シンプルなデプロイ、デバッグの容易さ、低レイテンシ
- ❌ スケーリングの制限、大規模なコードベース、デプロイリスク

```
src/
├── controllers/
├── services/
├── models/
├── repositories/
├── utils/
└── config/
```

### 7. Event-Driven

**構造:** イベント/メッセージを通じてコンポーネントが通信

- ✅ 疎結合、スケーラブル、リアルタイム処理
- ❌ デバッグの複雑さ、結果整合性、イベント順序の課題

```
src/
├── events/
│   ├── definitions/     # イベントスキーマ
│   └── handlers/        # イベントプロセッサー
├── publishers/          # イベント発行者
├── subscribers/         # イベントリスナー
└── services/
```

### 8. CQRS (Command Query Responsibility Segregation)

**構造:** データの読み取りと書き込みに別々のモデルを使用

- ✅ 読み取り/書き込みパフォーマンスの最適化、スケーラブル
- ❌ 複雑性の増加、結果整合性

```
src/
├── commands/            # 書き込み操作
│   ├── handlers/
│   └── models/
├── queries/             # 読み取り操作
│   ├── handlers/
│   └── models/
└── shared/
    └── events/
```

### 9. Domain-Driven Design (DDD)

**構造:** 境界づけられたコンテキスト、集約、ユビキタス言語を用いてビジネスドメインに沿ってモデル化されたソフトウェア

- ✅ コードとビジネスの整合性、複雑なロジックの処理に優れる
- ❌ 学習曲線が急、シンプルなCRUDアプリには過剰

```
src/
├── bounded-contexts/
│   ├── ordering/
│   │   ├── domain/      # 集約、エンティティ、値オブジェクト
│   │   ├── application/ # ユースケース、サービス
│   │   └── infrastructure/
│   └── shipping/
│       ├── domain/
│       ├── application/
│       └── infrastructure/
└── shared-kernel/       # 共有ドメイン概念
```
