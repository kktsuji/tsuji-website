---
title: "Github GistからBashスクリプトをダウンロードして実行"
description: ""
date: 2025-02-17T21:00:00+09:00
lastmod:
draft: false
---

## Github GistからBashスクリプトをダウンロードして実行

```bash
# ハッシュなしの最新バージョン
curl -fsSL https://gist.githubusercontent.com/mwufi/gist-url/raw/script-name.sh | sh

# ハッシュ付きの特定バージョン
curl -fsSL https://gist.githubusercontent.com/mwufi/gist-url/raw/hash/script-name.sh | sh
```

## Curlオプション

`curl`コマンドで使用される`-fsSL`オプションの詳細については、[tsuji.tech/curl-options-fssl](https://tsuji.tech/curl-options-fssl)を参照してください。
