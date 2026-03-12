---
title: "WSLでClaude Code CLIの通知を設定する方法"
description: ""
date: 2026-03-01T12:00:00+09:00
lastmod:
math: true
draft: false
---

## 概要

この記事では、WSLで動作するClaude Code CLIに対して、カスタム通知スクリプトとBurntToast PowerShellモジュールを使用してWindows Toast通知を設定する方法を紹介します。

- Windows PowershellにBurntToastをインストール
- WSLにPowerShell経由で通知を送信するスクリプトを作成
- Claude Code CLIが特定のhook（例: タスク完了時や操作が必要な時）で通知スクリプトを実行するように設定
- Claude Code CLIコマンドを実行し、Claude Codeからのメッセージを含むWindows Toast通知が届くことを確認

![img](https://img.tsuji.tech/claude-code-cli-notification-settings-wsl-0.jpg)

## PowershellにBurntToastをインストール

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

PowershellからテストとしてBurntToastの動作確認を行います:

```Powershell
Import-Module BurntToast
New-BurntToastNotification -Text "Test Notification", "BurntToast is working!"
```

## （オプション）通知用のカスタムロゴを設定

通知にカスタムロゴを使用するには、画像ファイル（例: `logo.png`）をWindowsのディレクトリに配置します。この記事では`D:\your\logo\path\logo.png`にロゴを配置します。以下のスクリプトの`ICON`変数をロゴのパスに更新してください。

カスタムロゴ付きの通知をテストできます:

```Powershell
Import-Module BurntToast
New-BurntToastNotification -Text "Test Notification", "BurntToast is working!" -AppLogo "D:\your\logo\path\logo.png"
```

## WSLでPowerShell経由の通知スクリプトを作成

スクリプトファイルを作成します。例えば`vim ~/.bin/claude-notify.sh`で以下の内容を記述します:

```bash
#!/bin/bash
# claude-notify.sh
# Claude Codeのhookがトリガーされた時にWindows Toast通知を送信するスクリプト
# Claude Codeはhookデータをstdin経由でJSONとして渡します

# 共通バイナリを利用可能にする（Claude CLIがシェルのPATHを継承しない場合があるため）
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH"

# stdinからJSONペイロードを読み取る
STDIN=$(cat)

# デバッグログ — 動作確認後に削除
{
  echo "=== $(date) ==="
  echo "STDIN: $STDIN"
} >> /tmp/claude-hook-debug.log 2>&1

# JSONからhookイベント名と最後のアシスタントメッセージを解析する
# メッセージをサニタイズ: PowerShellを壊す改行、Markdown、引用符を除去
HOOK=$(echo "$STDIN" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(d.get('hook_event_name', 'Claude Code'))
" 2>/dev/null)

LAST_MSG=$(echo "$STDIN" | python3 -c "
import sys, json, re
d = json.load(sys.stdin)
msg = d.get('last_assistant_message', '')
# Markdownコードブロックと見出しを除去
msg = re.sub(r'\`\`\`.*?\`\`\`', '', msg, flags=re.DOTALL)
msg = re.sub(r'[#*\`|]', '', msg)
# 空白と改行を単一スペースに圧縮
msg = re.sub(r'\s+', ' ', msg).strip()
# PowerShell文字列を壊さないようにシングル/ダブルクォートを除去
msg = msg.replace(\"'\", '').replace('\"', '')
# 80文字に切り詰め
print(msg[:80])
" 2>/dev/null)

# hookの種類に応じて通知タイトルとメッセージを設定
case "$HOOK" in
  "Stop")
    TITLE="Claude Code - Done"
    MESSAGE="${LAST_MSG:-Task completed!}"
    ;;
  "Notification")
    TITLE="Claude Code - Attention"
    MESSAGE="${LAST_MSG:-Needs your attention!}"
    ;;
  *)
    TITLE="Claude Code"
    MESSAGE="${LAST_MSG:-Notification}"
    ;;
esac

# WSLのアイコンパスをPowerShell用のWindowsパスに変換
ICON="/mnt/d/your/logo/path/logo.png"
WIN_ICON=$(wslpath -w "$ICON" 2>/dev/null)

# BurntToast PowerShellモジュール経由でWindows Toast通知を送信
/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -Command "
Import-Module BurntToast
New-BurntToastNotification -Text '$TITLE', '$MESSAGE' -AppLogo '$WIN_ICON'
" 2>/dev/null

# フォールバック: PowerShell通知が失敗した場合のターミナルベル
echo -e "\a"
```

スクリプトに実行権限を付与します:

```bash
sudo chmod +x ~/.bin/claude-notify.sh
```

## Claude Codeで通知スクリプトを使用するように設定

`vim ~/.claude/settings.json`でClaude Codeの設定を編集します:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "/home/your-username/.bin/claude-notify.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "/home/your-username/.bin/claude-notify.sh"
          }
        ]
      }
    ]
  }
}
```

`/home/your-username/.bin/claude-notify.sh`を実際の通知スクリプトのパスに置き換えてください。

上記の設定では、すべての`Notification`と`Stop`のhook（Claude Codeが注意を必要とする時やタスクが完了した時）で通知スクリプトがトリガーされます。特定のイベントのみで通知をトリガーしたい場合は、`matcher`フィールドをカスタマイズできます。

詳細は、[Claude Code Hooks reference](https://code.claude.com/docs/en/hooks)を参照ください。

## Claude Code CLIでテスト

プロジェクトディレクトリに移動し、Claude Code CLIを実行します:

```bash
cd your-project
claude
```

hookをトリガーするために簡単なリクエストを送信します。例えば:

```bash
❯ Hi

● Hi! How can I help you today?
```

すべて正しく設定されていれば、Claude Codeからのメッセージを含むWindows Toast通知が表示されます。

![img](https://img.tsuji.tech/claude-code-cli-notification-settings-wsl-0.jpg)

## デバッグ

通知が表示されない場合は、`/tmp/claude-hook-debug.log`のログを確認してください。

スクリプトの動作を確認した後、不要なログを避けるためにスクリプト`~/.bin/claude-notify.sh`からデバッグログの行を削除できます。

```bash
# デバッグログ — 動作確認後に削除
{
  echo "=== $(date) ==="
  echo "STDIN: $STDIN"
} >> /tmp/claude-hook-debug.log 2>&1
```
