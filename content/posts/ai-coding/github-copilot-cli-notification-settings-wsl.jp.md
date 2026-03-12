---
title: "WSLでGitHub Copilot CLIの通知を設定する方法"
description: ""
date: 2026-03-12T09:00:00+09:00
lastmod:
math: true
draft: false
---

## 概要

この記事では、カスタム通知スクリプトとBurntToast PowerShellモジュールを使用して、WSLで動作するGithub Copilot CLIのWindows Toast通知を設定する方法を紹介します。

- Windows PowershellにBurntToastをインストールする
- WSLにPowerShell経由で通知を送信する通知スクリプトを作成する
- 特定のイベント（セッション終了時やプロンプト送信時など）で通知スクリプトをトリガーするようにGithub Copilot CLIのhooksを設定する
- Github Copilot CLIコマンドを実行し、Windows Toast通知が届くことを確認してテストする

![img](https://img.tsuji.tech/github-copilot-cli-notification-settings-wsl-0.jpg)

## PowershellにBurntToastをインストールする

WSLからWindows Toast通知を送信するために、PowershellにBurntToastモジュールをインストールします。

```Powershell
Install-Module -Name BurntToast -Force -Scope CurrentUser
```

実行ポリシーがスクリプトの実行を許可しているか確認します:

```Powershell
Get-ExecutionPolicy -Scope CurrentUser
```

実行ポリシーが制限的すぎる場合（例: `Restricted`）、`RemoteSigned`に設定します:

```Powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Powershellからテスト通知を送信して、BurntToastが動作していることを確認できます:

```Powershell
Import-Module BurntToast
New-BurntToastNotification -Text "Test Notification", "BurntToast is working!"
```

## （任意）通知用のカスタムロゴを配置する

Windowsディレクトリに画像ファイル（例: `logo.png`）を配置することで、通知にカスタムロゴを使用できます。この記事では、ロゴを`D:\your\logo\path\logo.png`に配置します。以下のスクリプトの`ICON`変数をロゴのパスに更新してください。

カスタムロゴ付きの通知をテストできます:

```Powershell
Import-Module BurntToast
New-BurntToastNotification -Text "Test Notification", "BurntToast is working!" -AppLogo "D:\your\logo\path\logo.png"
```

## WSLに通知スクリプトを作成する

例えば`vim ~/.bin/copilot-notify.sh`でスクリプトファイルを作成し、以下の内容を追加します:

```bash
#!/bin/bash
# copilot-notify.sh
# Copilot CLIのhooksがトリガーされた時にWindows Toast通知を送信します。
# Copilot CLIはhookデータをJSON形式でstdin経由で渡します。
# hookイベント名はCOPILOT_HOOK_EVENT環境変数経由で渡されます。

# 一般的なバイナリが利用可能であることを保証する
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH"

# stdinからJSONペイロードを読み取る
STDIN=$(cat)

# デバッグログ — トラブルシューティング時にコメントを外してください
#{
#  echo "=== $(date) ==="
#  echo "COPILOT_HOOK_EVENT: $COPILOT_HOOK_EVENT"
#  echo "STDIN: $STDIN"
#} >> /tmp/copilot-hook-debug.log 2>&1

# hookイベントに基づいて通知のタイトルとメッセージを設定する
case "$COPILOT_HOOK_EVENT" in
  "sessionEnd")
    TITLE="Copilot - Done"
    MESSAGE="Session completed!"
    ;;
  "preToolUse")
    TITLE="Copilot - Action Needed"
    MESSAGE="Waiting for your input!"
    ;;
  "errorOccurred")
    TITLE="Copilot - Error"
    MESSAGE="An error occurred!"
    ;;
  *)
    TITLE="Copilot"
    MESSAGE="Notification"
    ;;
esac

# WSLアイコンパスをPowerShell用のWindowsパスに変換する
ICON="/mnt/d/your/logo/path/logo.png"
WIN_ICON=$(wslpath -w "$ICON" 2>/dev/null)

# BurntToast PowerShellモジュール経由でWindows Toast通知を送信する
/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -Command "
Import-Module BurntToast
New-BurntToastNotification -Text '$TITLE', '$MESSAGE' -AppLogo '$WIN_ICON'
" 2>/dev/null

# フォールバック: PowerShell通知が失敗した場合のターミナルベル
echo -e "\a"
```

スクリプトを実行可能にします:

```bash
chmod +x ~/.bin/copilot-notify.sh
```

## Copilot CLIのhooksを設定する

### hooks.jsonを作成する

hooks設定ファイルを作成します。`~/.copilot/hooks.json`に一元管理し、各プロジェクトにシンボリックリンクを作成します:

```json
{
  "version": 1,
  "hooks": {
    "sessionEnd": [
      {
        "type": "command",
        "bash": "/home/your-username/.bin/copilot-notify.sh",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "sessionEnd" }
      }
    ],
    "preToolUse": [
      {
        "type": "command",
        "bash": "/home/kktsuji/.bin/copilot-notify.sh",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "preToolUse" }
      }
    ],
    "errorOccurred": [
      {
        "type": "command",
        "bash": "/home/your-username/.bin/copilot-notify.sh",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "errorOccurred" }
      }
    ]
  }
}
```

`/home/your-username/.bin/copilot-notify.sh`を実際の通知スクリプトのパスに置き換えてください。

利用可能なhookイベントは以下の通りです:

| イベント              | 説明                       |
| --------------------- | -------------------------- |
| `sessionStart`        | セッション開始             |
| `sessionEnd`          | セッション完了             |
| `userPromptSubmitted` | ユーザーがプロンプトを送信 |
| `preToolUse`          | ツール使用前               |
| `postToolUse`         | ツール使用後               |
| `errorOccurred`       | エラー発生                 |

hooksの詳細については、[Using hooks with GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks)のドキュメントを参照してください。

### プロジェクトにhooks.jsonをシンボリックリンクする

Copilot CLIはカレントディレクトリの`.github/hooks/hooks.json`からhooksを読み込みます。通知を有効にしたい各プロジェクトにシンボリックリンクを作成します:

```bash
mkdir -p your-project/.github/hooks
ln -s ~/.copilot/hooks.json your-project/.github/hooks/hooks.json
```

これにより、単一の`hooks.json`を管理し、複数のプロジェクトで共有できます。

## Copilot CLIでテストする

プロジェクトディレクトリに移動してCopilot CLIを実行します:

```bash
cd your-project
copilot
```

次に、hooksをトリガーするために小さなリクエストを送信します。例えば:

```bash
> hi
```

すべてが正しく設定されていれば、以下のタイミングでWindows Toast通知が表示されるはずです:

- セッション終了時（`sessionEnd`）
- エラー発生時（`errorOccurred`）

![img](https://img.tsuji.tech/github-copilot-cli-notification-settings-wsl-0.jpg)

## デバッグ

通知が表示されない場合は、`~/.bin/copilot-notify.sh`のデバッグブロックのコメントを外してデバッグログを有効にします:

```bash
# デバッグログ — トラブルシューティング時にコメントを外してください
{
  echo "=== $(date) ==="
  echo "COPILOT_HOOK_EVENT: $COPILOT_HOOK_EVENT"
  echo "STDIN: $STDIN"
} >> /tmp/copilot-hook-debug.log 2>&1
```

その後、`/tmp/copilot-hook-debug.log`のログを確認します:

```bash
cat /tmp/copilot-hook-debug.log
```

Copilot CLIの実行後にログファイルが存在しない場合、hooksが読み込まれていません。以下を確認してください:

1. シンボリックリンクが有効であること: `ls -la your-project/.github/hooks/hooks.json`
2. hooks.jsonのパスが`.github/hooks/hooks.json`であること（プロジェクトルートではない）
3. 通知スクリプトが実行可能であること: `ls -la ~/.bin/copilot-notify.sh`

スクリプトを直接テストすることもできます:

```bash
echo '{"timestamp":1704614400000}' | COPILOT_HOOK_EVENT=sessionEnd ~/.bin/copilot-notify.sh
```

セットアップの動作が確認できたら、不要なログを避けるためにデバッグログの行をコメントアウトしてください。
