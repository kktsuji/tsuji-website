---
title: "arXiv新着論文をWebhookへ自動通知するためのAWSの設定"
description: "arXiv新着論文をWebhookへ自動通知するためのAWSの設定を解説する記事。"
date: 2024-08-03T15:27:14+09:00
lastmod: 2024-08-11T08:30:00+09:00
draft: false
---

## 事前準備

### 環境の確認

まず、開発環境の確認を行う。Ubuntu 22.04.4 LTSのみサポートしている。

```bash
lsb_release -a
# Ubuntu 22.04.4 LTS

uname -m
# x86_64
```

### AWS Lambda LayerのためにZipファイルを作成

筆者のgithubプロジェクト[arxiv-bot](https://github.com/kktsuji/arxiv-bot)をクローン。

```bash
git clone git@github.com:kktsuji/arxiv-bot.git
cd arxiv-bot
```

Pythonのバージョンは3.12.3でなければならない。

```python
python --version
# Python 3.12.3
```

新しいディレクトリを作成し、そこにpythonパッケージをインストールする。次にzipファイルを作成する。ここで、zipファイルの名前は`python.zip`でなければならない点に注意。このファイルはAWSのラムダレイヤーで使用される。

```bash
mkdir python
pip install -U pip
pip install -r requirements.txt -t ./python
zip -r python.zip ./python
```

## Webhookの設定

通知したいサービスのwebhook urlを取得する。

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [Microsoft Teams Webhooks](https://learn.microsoft.com/en-us/power-automate/teams/create-flows-power-apps-app)
- [Discord Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
- etc.

## （任意）OpenAIの設定

ChatGPTによる論文のサマリを生成したい場合、OpenAI API Keyを取得する。

注意：OpenAI APIは有料。

- [OpenAI API](https://openai.com/api/)

## AWS Lambdaの設定

### Lambda Layer

[AWS Lambda Console](https://aws.amazon.com/lambda/)へアクセスし、"Create layer"を行う。

先ほど作成した`python.zip`ファイルをアップロードし、"compatible architectures"ではZipファイルを作成した開発環境のアーキテクチャを選択する。ランタイムはPython 3.12を選ぶ。

注意：Zipファイルの名前が`python.zip`出ない場合、lambda関数実行時のサードパーティ製Pythonモジュールのインポートが失敗する。

![img](https://img.tsuji.tech/arxiv-bot-aws-0.jpg)

### Lambda Function

AWSラムダコンソールで"Create function"を行う。

"Author from scratch"を選択し、項目を正しく記載する。

![img](https://img.tsuji.tech/arxiv-bot-aws-1.jpg)

関数作成後、"Add a layer"ページを開く。

![img](https://img.tsuji.tech/arxiv-bot-aws-2.jpg)

"Custom layers"を選択し、先ほど作成したレイヤーとそのバージョンを指定する。

![img](https://img.tsuji.tech/arxiv-bot-aws-3.jpg)

[arxiv-bot](https://github.com/kktsuji/arxiv-bot)プロジェクトの`main.py`のコード全体をコピーし、"Code" > "Code source" > `lambda_function.py`を上書きして貼り付ける。

そして、"Deploy"ボタンを押下する。

![img](https://img.tsuji.tech/arxiv-bot-aws-4.jpg)

次に"Test"を押下し、"Configure test event"のフォームを記載する。

"Event JSON"の項目は、以下のフォーマットに従って記入する必要がある（これらのパラメータは関数のテストでのみ使用される）。

```json
{
  "webhook_url": "https://YOUR_WEBHOOK_URL",
  "keywords": "keyword1,keyword2,keyword3",
  "categories": "cs.AI,cs.CV,cs.LG,eess.IV",
  "openai_api_key": "YOUR_API_KEY"
}
```

| Key            | Description                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| webhook_url    | Slack, Teams, その他のサービスのAPIのwebhook url。                                                                                                                                                                                                                                                                                                                                               |
| keywords       | arXiv検索のクエリーで使用されるキーワード。<br>各キーワードはスペース無しの半角コンマで区切る。<br>キーワードはタイトルとアブストラクトの検索に使用され、それぞれ"or"で検索される。<br>例えば、"keyword1,key word2"と指定すると、keyword1を含む論文と'key word2'を含む論文が検索結果として表示される。（もしキーワード内にスペースを含む場合、シングルクォーテーションで囲んで検索に使用される） |
| categories     | arXiv検索のクエリで使用されるカテゴリー。<br>これはキーワードと同じルールに従う（スペースなしの半角カンマ区切り、"or"で検索）。また、半角スペースは無視される。<br>詳細は[arXiv Category Taxonomy](https://arxiv.org/category_taxonomy)を参照。                                                                                                                                                  |
| OPENAI_API_KEY | （任意）OpenAI API Key.<br>もし論文のサマリ作成機能を使用しない場合は、以下のように空白を指定する：<br>`"openai_api_key": ""`                                                                                                                                                                                                                                                                    |

![img](https://img.tsuji.tech/arxiv-bot-aws-5.jpg)

設定を保存し、テストを実行する。

実行結果は"Code source"で確認できる。もしくは、Webhook URLで指定したサービスでも確認ができる。

![img](https://img.tsuji.tech/arxiv-bot-aws-6.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-7.jpg)

動作確認の後、Lambda関数の"ARN"をメモする。

![img](https://img.tsuji.tech/arxiv-bot-aws-16.jpg)

## AWS IAMの設定

Lambda関数を実行するためのポリシーを作成する。

### IAM Policy

[AWS IAM](https://aws.amazon.com/iam/) > Policies > "Create policy"で以下のポリシーを作成。

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

AWS IAM > Roles > "Create role"で以下のロールを作成。

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

## AWS EventBridgeの設定

ラムダ関数を毎日決まった時間に実行するための設定。

### EventBridge Schedule

[AWS EventBridge Console](https://aws.amazon.com/eventbridge/)へアクセスし、"Create schedule"を行う。

![img](https://img.tsuji.tech/arxiv-bot-aws-8.jpg)

フォームを記入する。ラムダ関数を正しい時刻に実行するために、タイムゾーンの設定とcronの設定をよく確認する。

![img](https://img.tsuji.tech/arxiv-bot-aws-9.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-10.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-11.jpg)

arXiv検索結果を得るためにJSONパラメータを正しく設定すること（これらのパラメータは毎日のクエリで使用される）。

```json
{
  "webhook_url": "https://YOUR_WEBHOOK_URL",
  "keywords": "keyword1,keyword2,keyword3",
  "categories": "cs.AI,cs.CV,cs.LG,eess.IV",
  "openai_api_key": "YOUR_API_KEY"
}
```

![img](https://img.tsuji.tech/arxiv-bot-aws-12.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-13.jpg)

残りのフォームも記入する。

![img](https://img.tsuji.tech/arxiv-bot-aws-14.jpg)

作成したIAMポリシーを、Permission > Execution role > Use existing role > Role nameへ設定。

![img](https://img.tsuji.tech/arxiv-bot-aws-15.jpg)

スケジュールを作成。

以上で設定は完了。
