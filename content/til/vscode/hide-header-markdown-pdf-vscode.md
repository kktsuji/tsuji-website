---
title: 'Hide Header in Markdown PDF for VSCode'
description: ''
date: 2025-04-08T16:00:00+09:00
lastmod: 
draft: false
---

## Hide Header in Markdown PDF for VSCode

Add workspace settings `.vscode/settings.json`:

```json
{
  "markdown-pdf.headerTemplate": "<div></div>"
}
```

## Reference

- [Markdown PDF's README.md - Github](https://github.com/yzane/vscode-markdown-pdf/blob/master/README.md#markdown-pdfheadertemplate)
