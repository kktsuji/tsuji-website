---
title: "WindowsでのGithub Copilot CLIの通知設定"
description: ""
date: 2026-04-22T09:00:00+09:00
lastmod:
math: true
draft: false
---

## 概要

この記事では、カスタム通知スクリプトとBurntToastというPowerShellモジュールを使用して、Windows上で実行されるGithub Copilot CLIのWindowsトースト通知を設定する方法を紹介します。

- Windows PowerShellでBurntToastをインストールする
- Windowsトースト通知を送信する通知スクリプトをPowerShellで作成する
- 特定のイベント(セッション終了時やプロンプト送信時など)で通知スクリプトをトリガーするようにGithub Copilot CLIのフックを設定する
- Github Copilot CLIコマンドを実行し、Windowsトースト通知が受信できるか確認して設定をテストする

![img](https://img.tsuji.tech/github-copilot-cli-notification-settings-wsl-0.jpg)

## PowerShellでのBurntToastのインストール

Windowsトースト通知を送信するために、PowerShellにBurntToastモジュールをインストールします。

```PowerShell
Install-Module -Name BurntToast -Force -Scope CurrentUser
```

実行ポリシーでスクリプトの実行が許可されていることを確認します。

```PowerShell
Get-ExecutionPolicy -Scope CurrentUser
```

実行ポリシーが厳しすぎる場合(例:`Restricted`)、`RemoteSigned`に設定します。

```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

PowerShellからテスト通知を送信して、BurntToastが動作していることを確認できます。

```PowerShell
Import-Module BurntToast
New-BurntToastNotification -Text "テスト通知", "BurntToastは動作しています!"
```

## (オプション)通知用のカスタムロゴを設定する

画像ファイル(例:`logo.png`)をWindowsのディレクトリに配置することで、通知にカスタムロゴを使用できます。この記事では、ロゴを`D:\your\logo\path\logo.png`に配置します。以下のスクリプト内の`$icon`変数を、使用するロゴのパスに更新してください。

カスタムロゴ付きの通知をテストできます。

```PowerShell
Import-Module BurntToast
New-BurntToastNotification -Text "テスト通知", "BurntToastは動作しています!" -AppLogo "D:\your\logo\path\logo.png"
```

## PowerShellで通知スクリプトを作成する

スクリプトファイルを作成します。例えば`notepad $env:USERPROFILE\.bin\copilot-notify.ps1`を実行し、以下の内容を追加します。

```PowerShell
# copilot-notify.ps1
# Copilot CLIのフックがトリガーされた時にWindowsトースト通知を送信します。
# Copilot CLIは標準入力(stdin)経由でフックデータをJSONとして渡します。
# フックのイベント名はCOPILOT_HOOK_EVENT環境変数経由で渡されます。

# 標準入力からJSONペイロードを読み込む
$stdin = $input | Out-String

# デバッグログ — トラブルシューティング時にコメントアウトを解除する
#$logPath = "$env:TEMP\copilot-hook-debug.log"
#"=== $(Get-Date) ===" | Add-Content $logPath
#"COPILOT_HOOK_EVENT: $env:COPILOT_HOOK_EVENT" | Add-Content $logPath
#"STDIN: $stdin" | Add-Content $logPath

# フックイベントに基づいて通知のタイトルとメッセージを設定する
switch ($env:COPILOT_HOOK_EVENT) {
    "sessionEnd" {
        $title = "Copilot - 完了"
        $message = "セッションが完了しました!"
    }
    "preToolUse" {
        $title = "Copilot - アクションが必要"
        $message = "入力待ちです!"
    }
    "errorOccurred" {
        $title = "Copilot - エラー"
        $message = "エラーが発生しました!"
    }
    default {
        $title = "Copilot"
        $message = "通知"
    }
}

$icon = "D:\your\logo\path\logo.png"

# BurntToast経由でWindowsトースト通知を送信する
Import-Module BurntToast
New-BurntToastNotification -Text $title, $message -AppLogo $icon
```

`.bin`ディレクトリが存在しない場合は作成し、スクリプトが配置されていることを確認します。

```PowerShell
New-Item -ItemType Directory -Path "$env:USERPROFILE\.bin" -Force
```

## Copilot CLIフックの設定

### hooks.jsonの作成

フックの設定ファイルを作成します。`%USERPROFILE%\.copilot\hooks.json`に一元的に保存し、各プロジェクトにシンボリックリンクを作成します。

```json
{
  "version": 1,
  "hooks": {
    "sessionEnd": [
      {
        "type": "command",
        "command": "powershell.exe -NonInteractive -File C:\\Users\\your-username\\.bin\\copilot-notify.ps1",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "sessionEnd" }
      }
    ],
    "preToolUse": [
      {
        "type": "command",
        "command": "powershell.exe -NonInteractive -File C:\\Users\\your-username\\.bin\\copilot-notify.ps1",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "preToolUse" }
      }
    ],
    "errorOccurred": [
      {
        "type": "command",
        "command": "powershell.exe -NonInteractive -File C:\\Users\\your-username\\.bin\\copilot-notify.ps1",
        "timeoutSec": 10,
        "env": { "COPILOT_HOOK_EVENT": "errorOccurred" }
      }
    ]
  }
}
```

`C:\Users\your-username\.bin\copilot-notify.ps1`を通知スクリプトの実際のパスに置き換えてください。

利用可能なフックイベントは以下の通りです。

| イベント              | 説明                       |
| --------------------- | -------------------------- |
| `sessionStart`        | セッションの開始           |
| `sessionEnd`          | セッションの完了           |
| `userPromptSubmitted` | ユーザーがプロンプトを送信 |
| `preToolUse`          | ツール使用前               |
| `postToolUse`         | ツール使用後               |
| `errorOccurred`       | エラーの発生               |

フックの詳細については、[Using hooks with GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks)のドキュメントを参照してください。

### プロジェクトへのhooks.jsonのシンボリックリンク

Copilot CLIは、現在の作業ディレクトリの`.github\hooks\hooks.json`からフックを読み込みます。通知を受け取りたい各プロジェクトにシンボリックリンクを作成します(PowerShellを管理者として実行します)。

```PowerShell
New-Item -ItemType Directory -Path "your-project\.github\hooks" -Force

# Windowsでシンボリックリンクを作成するには管理者権限が必要です。PowerShellを管理者として実行し、以下を実行します:
New-Item -ItemType SymbolicLink -Path "your-project\.github\hooks\hooks.json" -Target "$env:USERPROFILE\.copilot\hooks.json"
```

この方法により、単一の`hooks.json`を維持し、複数のプロジェクト間で共有することができます。

## Copilot CLIでのテスト

プロジェクトディレクトリに移動し、Copilot CLIを実行します。

```PowerShell
cd your-project
copilot
```

次に、フックをトリガーするために短いリクエストを送信します。例えば:

```text
> hi
```

設定が正しければ、以下の場合にWindowsトースト通知が表示されるはずです。

- セッション終了時(`sessionEnd`)
- エラー発生時(`errorOccurred`)

![img](https://img.tsuji.tech/github-copilot-cli-notification-settings-wsl-0.jpg)

## デバッグ

通知が表示されない場合は、`copilot-notify.ps1`でデバッグブロックのコメントアウトを解除し、デバッグログを有効にしてください。

```PowerShell
# デバッグログ — トラブルシューティング時にコメントアウトを解除する
$logPath = "$env:TEMP\copilot-hook-debug.log"
"=== $(Get-Date) ===" | Add-Content $logPath
"COPILOT_HOOK_EVENT: $env:COPILOT_HOOK_EVENT" | Add-Content $logPath
"STDIN: $stdin" | Add-Content $logPath
```

その後、`%TEMP%\copilot-hook-debug.log`でログを確認します。

```PowerShell
Get-Content "$env:TEMP\copilot-hook-debug.log"
```

Copilot CLI実行後にログファイルが存在しない場合、フックは読み込まれていません。以下を確認してください。

1. シンボリックリンクが有効であるか: `Get-Item your-project\.github\hooks\hooks.json`
2. hooks.jsonのパスが`.github\hooks\hooks.json`であるか(プロジェクトルートではない)
3. hooks.json内の通知スクリプトのパスが正しいか

PowerShellから直接スクリプトをテストすることもできます。

```PowerShell
$env:COPILOT_HOOK_EVENT = "sessionEnd"
'{"timestamp":1704614400000}' | powershell.exe -NonInteractive -File "$env:USERPROFILE\.bin\copilot-notify.ps1"
```

設定が機能していることを確認した後、不要なログを避けるためにデバッグログの行をコメントアウトしてください。
