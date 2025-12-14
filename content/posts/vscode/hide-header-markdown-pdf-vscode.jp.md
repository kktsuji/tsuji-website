---
title: "VSCodeのMarkdown PDFでヘッダーを非表示にする"
description: ""
date: 2025-04-08T16:00:00+09:00
lastmod:
draft: false
---

## VSCodeのMarkdown PDFでヘッダーを非表示にする

ワークスペース設定`.vscode/settings.json`に追加する：

```json
{
  "markdown-pdf.headerTemplate": "<div></div>"
}
```

## 参考文献

- [Markdown PDF's README.md - Github](https://github.com/yzane/vscode-markdown-pdf/blob/master/README.md#markdown-pdfheadertemplate)
