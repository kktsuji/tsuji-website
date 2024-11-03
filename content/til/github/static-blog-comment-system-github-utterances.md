---
title: 'GitHub Issues Based Comment System "utterances" for Static Website'
description: ''
date: 2024-11-03T20:00:00+09:00
lastmod: 
draft: false
---

[utterances](https://github.com/utterance/utterances) is a cool tool built on GitHub for embedding comment forms on static websites.

Merits:

- Free, lightweight and looks cool
- Comments are stored on GitHub issues on my repository
- GitHub login is required to comment (preventing spam)

Demerits:

- Visitors without a Github account can't comment (no problem for tech blog).

Installation is so easy:

1. Install [utterances App](https://github.com/apps/utterances) in your repository. (utterances-bot writes comments on Issues of this repository. Use a blog repository or create new repository only for comments)
2. utterances installation page creates a javascript for comment form.
3. Add the script to blog code.

Script is like following:

```javascript
<script src="https://utteranc.es/client.js"
    repo="account/repository"
    issue-term="pathname"
    label="comment"
    theme="github-dark"
    crossorigin="anonymous"
    async>
</script>
```

My blog already uses utterances comment system like below in this page.
