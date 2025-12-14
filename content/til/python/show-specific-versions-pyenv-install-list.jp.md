---
title: "pyenv install --listで特定のバージョンを表示する"
description: ""
date: 2025-10-15T09:00:00+09:00
lastmod:
draft: false
---

## 特定のバージョンを表示する

```bash
# Show only Python 3.x versions
pyenv install -l | grep "^  3\."

# Show only Python 2.x versions
pyenv install --list | grep "^  2\."
```

- `^`: 行の先頭
- `  `: 2つのスペース（pyenv install --listの出力形式）
- `3\.`: 「3.」にマッチ（正規表現でドット`.`は任意の文字を意味するため、`\`でエスケープする）
