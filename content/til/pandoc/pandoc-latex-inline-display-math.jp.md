---
title: "Pandoc LaTeXのインライン数式とディスプレイ数式"
description: ""
date: 2025-04-17T18:00:00+09:00
lastmod:
draft: false
math: true
---

## Pandoc LaTeXインライン数式スタイル

インラインTeX式には`$`を使用します。

```markdown
$E=mc^2$
```

これは$ E = mc^2 $としてレンダリングされます。

## Pandoc LaTeXディスプレイ数式スタイル

ディスプレイTeX式には`$$`を使用します。

```markdown
$$
E=mc^2
$$
```

または

```markdown
\[
E=mc^2
\]
```

これは次のようにレンダリングされます：

$$
E=mc^2
$$
