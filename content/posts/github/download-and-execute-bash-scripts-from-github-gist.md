---
title: "Download and Execute Bash Scripts from Github Gist"
description: ""
date: 2025-02-17T21:00:00+09:00
lastmod:
draft: false
---

## Download and Execute Bash Scripts from Github Gist

```bash
# Latest version without hash
curl -fsSL https://gist.githubusercontent.com/mwufi/gist-url/raw/script-name.sh | sh

# Specific version with hash
curl -fsSL https://gist.githubusercontent.com/mwufi/gist-url/raw/hash/script-name.sh | sh
```

## Curl Options

See [tsuji.tech/curl-options-fssl](https://tsuji.tech/curl-options-fssl) for a breakdown of the `-fsSL` options used with the `curl` command.
