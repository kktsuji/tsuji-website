---
title: 'AWS Configuration to Automatically Notify Webhooks of New Papers on arXiv'
description: 'Post about AWS Configuration to Automatically Notify Webhooks of New Papers on arXiv.'
date: 2024-08-03T15:27:14+09:00
lastmod: 2024-08-11T08:30:00+09:00
draft: false
---

## Preparation

### Check Environment

Check your environment. Ubuntu 22.04.4 LTS is only supported.

```bash
lsb_release -a
# Ubuntu 22.04.4 LTS

uname -m
# x86_64
```

### Create Zip for AWS Lambda Layer

Clone my github project [arxiv-bot](https://github.com/kktsuji/arxiv-bot).

```bash
git clone git@github.com:kktsuji/arxiv-bot.git
cd arxiv-bot
```

Python version must be 3.12.3.

```python
python --version
# Python 3.12.3
```

Create new directory and install python packages to the directory. Then create zip file. The zip file name must be ``python.zip``. This file will used for aws lambda layer.

```bash
mkdir python
pip install -U pip
pip install -r requirements.txt -t ./python
zip -r python.zip ./python
```

## Webhook Settings

Get webhook url of the service you want to notify.

* [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
* [Microsoft Teams Webhooks](https://learn.microsoft.com/en-us/power-automate/teams/create-flows-power-apps-app)
* [Discord Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
* etc.

## (Optional) OpenAI Settings

Get OpenAI API Key if you want to summary papers.

Note: The OpenAI API is chargeable.

* [OpenAI API](https://openai.com/api/)

## AWS Lambda Settings

### Lambda Layer

Visit [AWS Lambda Console](https://aws.amazon.com/lambda/) and "Create layer".

Upload ``python.zip`` file and fill "compatible architectures" of your environment that created the zip file. And set Python 3.12 to Runtime.

Note: If the file name is not ``python.zip``, lambda function will fail to import third-party python modules.

![img](https://img.tsuji.tech/arxiv-bot-aws-0.jpg)

### Lambda Function

Visit "Create function" in AWS Lambda Console.

Select "Author from scratch" and fill forms correctly.

![img](https://img.tsuji.tech/arxiv-bot-aws-1.jpg)

After creating function, visit "Add a layer" page.

![img](https://img.tsuji.tech/arxiv-bot-aws-2.jpg)

Select "Custom layers" and the layer you created and its version.

![img](https://img.tsuji.tech/arxiv-bot-aws-3.jpg)

Copy entire code of ``main.py`` in [arxiv-bot](https://github.com/kktsuji/arxiv-bot) project, and past it to "Code" > "Code source" > ``lambda_function.py``.

And push "Deploy" button.

![img](https://img.tsuji.tech/arxiv-bot-aws-4.jpg)

Push "Test" and fill the "Configure test event".

The "Event JSON" must follow this format (these parameters are used for only test).

```json
{
  "webhook_url": "https://YOUR_WEBHOOK_URL",
  "keywords": "keyword1,keyword2,keyword3",
  "categories": "cs.AI,cs.CV,cs.LG,eess.IV",
  "openai_api_key": "YOUR_API_KEY"
}
```

| Key | Description |
|----------|----------|
| webhook_url | The webhook url such as Slack, Teams, and other service APIs. |
| keywords | Keywords used in queries for arXiv searches.<br>Each keyword is separated by a comma with no spaces.<br>Keywords are used to search titles and abstracts and are searched for with "or".<br>For example, if the value "keyword1,key word2" is specified, paper containing keyword1 and papers containing 'key word2' will be displayed as search results (if a keyword contains spaces, single quotation marks are be used). |
| categories | Categories used in queries for arXiv searches.<br>This follows the same rule of keywords (separated by comma without space, searched with "or"). And spaces are removed.<br>For more details, see [arXiv Category Taxonomy](https://arxiv.org/category_taxonomy). |
| OPENAI_API_KEY | (Optional) OpenAI API Key.<br>If you do not use the paper summarization function, please leave blank like bellow:<br>``"openai_api_key": ""`` |

![img](https://img.tsuji.tech/arxiv-bot-aws-5.jpg)

Save configuration and execute test.

Execution results can be checked in "Code source" or at the service of the webhook URL you wrote.

![img](https://img.tsuji.tech/arxiv-bot-aws-6.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-7.jpg)

Once the operation is checked, note the "Function ARN" of the Lambda function.

![img](https://img.tsuji.tech/arxiv-bot-aws-16.jpg)

## AWS IAM Settings

Create policy to invoke Lambda function.

### IAM Policy

Visit [AWS IAM](https://aws.amazon.com/iam/) > Policies > "Create policy".

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

Visit AWS IAM > Roles > "Create role".

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

Then attach the policy to the role.

## AWS EventBridge Settings

Setup to execute Lambda functions at a fixed time each day.

### EventBridge Schedule

Visit [AWS EventBridge Console](https://aws.amazon.com/eventbridge/) and "Create schedule".

![img](https://img.tsuji.tech/arxiv-bot-aws-8.jpg)

Fill the forms. Please confirm the timezone setting and the cron setting to execute the Lambda function at the correct time.

![img](https://img.tsuji.tech/arxiv-bot-aws-9.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-10.jpg)

![img](https://img.tsuji.tech/arxiv-bot-aws-11.jpg)

Correctly set json parameters to obtain arXiv search results (these parameters are used for daily queries).

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

Fill remaining forms.

![img](https://img.tsuji.tech/arxiv-bot-aws-14.jpg)

Set IAM Policy you created to Permission > Execution role > Use existing role > Role name.

![img](https://img.tsuji.tech/arxiv-bot-aws-15.jpg)

Create schedule.

Settings completed!
