---
title: 'arXiv 新着論文を Webhook へ自動通知するための AWS の設定'
description: 'arXiv 新着論文を Webhook へ自動通知するための AWS の設定を解説する記事。'
date: 2024-08-03T15:27:14+09:00
lastmod: 2024-08-05T06:42:00+09:00
math: false
draft: false
---

## 事前準備

### 環境の確認

まず、開発環境の確認を行う。Ubuntu 22.04.4 LTS のみサポートしている。

```bash
lsb_release -a
# Ubuntu 22.04.4 LTS

uname -m
# x86_64
```

### AWS Lambda Layer のために Zip ファイルを作成

筆者の github プロジェクト [arxiv-bot](https://github.com/kktsuji/arxiv-bot) をクローン.

```bash
git clone git@github.com:kktsuji/arxiv-bot.git
cd arxiv-bot
```

Python のバージョンは 3.12.3 でなければならない.

```python
python --version
# Python 3.12.3
```

新しいディレクトリを作成し、そこに python パッケージをインストールする。次に zip ファイルを作成する。ここで、zip ファイルの名前は ``python.zip`` でなければならない点に注意。このファイルは AWS のラムダレイヤーで使用される。

```bash
mkdir python
pip install -U pip
pip install -r requirements.txt -t ./python
zip -r python.zip ./python
```

## AWS Lambda の設定

### Lambda Layer

[AWS Lambda Console](https://aws.amazon.com/lambda/) へアクセスし、"Create layer" を行う。

先ほど作成した ``python.zip`` ファイルをアップロードし、"compatible architectures" では Zip ファイルを作成した開発環境のアーキテクチャを選択する。ランタイムは Python 3.12 を選ぶ。

注意：Zip ファイルの名前が ``python.zip`` 出ない場合、lambda 関数実行時のサードパーティ製 Python モジュールのインポートが失敗する。

![img](https://img.tsuji.tech/arxiv-bot-aws-0.jpg)

### Lambda Function

AWS ラムダコンソールで "Create function" を行う。

"Author from scratch" を選択し、項目を正しく記載する。

![img](https://img.tsuji.tech/arxiv-bot-aws-1.jpg)

関数作成後、"Add a layer" ページを開く。

![img](https://img.tsuji.tech/arxiv-bot-aws-2.jpg)

"Custom layers" を選択し、先ほど作成したレイヤーとそのバージョンを指定する。

![img](https://img.tsuji.tech/arxiv-bot-aws-3.jpg)

[arxiv-bot](https://github.com/kktsuji/arxiv-bot) プロジェクトの ``main.py`` のコード全体をコピーし、"Code" > "Code source" > ``lambda_function.py`` を上書きして貼り付ける。

そして、"Deploy" ボタンを押下する。

![img](https://img.tsuji.tech/arxiv-bot-aws-4.jpg)

次に "Test" を押下し、"Configure test event" のフォームを記載する。

"Event JSON" の項目は、以下のフォーマットに従って記入する必要がある（これらのパラメータは関数のテストでのみ使用される）。

```json
{
  "webhook_url": "https://YOUR_WEBHOOK_URL",
  "keywords": "keyword1,keyword2,keyword3",
  "categories": "cs.AI,cs.CV,cs.LG,eess.IV"
}
```

| Key | Description |
|----------|----------|
| webhook_url | Slack, Teams, その他のサービスの API の webhook url。 |
| keywords | arXiv検索のクエリーで使用されるキーワード。<br>各キーワードは半角コンマで区切り、スペースは入れない。<br>キーワードはタイトルとアブストラクトの検索に使用される。<br>各キーワードは "or "で検索される。<br>例えば、"keyword1,keyword2 "と指定すると、"keyword1 "を含む論文と "keyword2 "を含む論文が検索結果として表示される。<br>より具体的な例を挙げると、値として "deep learning, contrastive learning" を与えられた場合、"deep,contrastive,learning" と等価となる (半角スペースはカンマで置換され、重複した単語は無視される)。 |
| categories | arXiv 検索のクエリで使用されるカテゴリー。<br>これはキーワードと同じルールに従う（スペースなしの半角カンマ区切り、"or "で検索）。また、半角スペースは無視される。<br>詳細は [arXiv Category Taxonomy](https://arxiv.org/category_taxonomy) を参照. |

![img](https://img.tsuji.tech/arxiv-bot-aws-5.jpg)

設定を保存し、テストを実行する。

実行結果は "Code source" で確認できる。もしくは、Webhook URL で指定したサービスでも確認ができる。

![img](https://img.tsuji.tech/arxiv-bot-aws-6.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-7.jpg)

動作確認の後、Lambda 関数の "ARN" をメモする。

![img](https://img.tsuji.tech/arxiv-bot-aws-16.jpg)

## AWS IAM の設定

Lambda 関数を実行するためのポリシーを作成する。

### IAM Policy

[AWS IAM](https://aws.amazon.com/iam/) > Policies > "Create policy" で以下のポリシーを作成。

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:YOUR-LAMBDA-FUNCTION-ARN"
        }
    ]
}
```

### IAM Role

AWS IAM > Roles > "Create role" で以下のロールを作成。

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "admitEventBridge",
            "Effect": "Allow",
            "Principal": {
                "Service": "scheduler.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

作成後、ロールにポリシーをアタッチしておく。

## AWS EventBridge の設定

ラムダ関数を毎日決まった時間に実行するための設定。

### EventBridge Schedule

[AWS EventBridge Console](https://aws.amazon.com/eventbridge/) へアクセスし、"Create schedule" を行う。

![img](https://img.tsuji.tech/arxiv-bot-aws-8.jpg)


フォームを記入する。ラムダ関数を正しい時刻に実行するために、タイムゾーンの設定と cron の設定をよく確認する。

![img](https://img.tsuji.tech/arxiv-bot-aws-9.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-10.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-11.jpg)

arXiv 検索結果を得るために JSON パラメータを正しく設定すること（これらのパラメータは毎日のクエリで使用される）。

```json
{
  "webhook_url": "https://YOUR_WEBHOOK_URL",
  "keywords": "keyword1,keyword2,keyword3",
  "categories": "cs.AI,cs.CV,cs.LG,eess.IV"
}
```

![img](https://img.tsuji.tech/arxiv-bot-aws-12.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-13.jpg)

残りのフォームも記入する。

![img](https://img.tsuji.tech/arxiv-bot-aws-14.jpg)

作成した AIM ポリシーを、Permission > Execution role > Use existing role > Role name へ設定。

![img](https://img.tsuji.tech/arxiv-bot-aws-15.jpg)

スケジュールを作成。

以上で設定は完了。
