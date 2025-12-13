---
title: 'Comment System "Giscus" Built on GitHub Discussions for Static Website'
description: ""
date: 2024-11-04T09:00:00+09:00
lastmod:
draft: false
---

## Overview

[Giscus](https://github.com/giscus/giscus) is a comment system built on GitHub Discussions for embedding comment forms on static websites.

Merits:

- Free, lightweight and looks cool
- Comments are stored on GitHub Discussions of my repository
- GitHub login is required to comment (preventing spam)

Demerits:

- Visitors without a Github account can't comment (but no problem for tech blog)

## Giscus vs utterances

Giscus is strongly inspired by [utterances](https://github.com/utterance/utterances). Main concepts and usages are almost same but there are some differences.

- Gisccus
  - Use GitHub Discussions to store comments
  - Richer features (e.g. reaction, voting) than utterances
- utterances
  - Use Github Issues to save comments

I adopted Giscus for this blog because I felt that GitHub Discussions is better to store comments than GitHub Issues.

## Installation

Installation steps:

1. Enable Discussions feature in a repository (see [GitHub document](https://docs.github.com/en/discussions)) (giscus-bot writes comments on Discussions of this repository. Use a blog repository or create new repository only for comments)
2. Install [Giscus App](https://github.com/apps/giscus) in the repository.
3. Create a javascript on [giscus.app](https://giscus.app/). Some options can be customized.
4. Copy the script and add it to blog code.

An example script is following:

```javascript
<script
  src="https://giscus.app/client.js"
  data-repo="user/repository"
  data-repo-id="xxxxxxx"
  data-category="Comments"
  data-category-id="xxxxxx"
  data-mapping="pathname"
  data-strict="0"
  data-reactions-enabled="1"
  data-emit-metadata="0"
  data-input-position="top"
  data-theme="dark"
  data-lang="en"
  crossorigin="anonymous"
  async
></script>
```

## Dynamic Theme Changing

Dynamically changing the theme of Giscus as the page theme changes requires some coding.

I refer to [this comment](https://github.com/giscus/giscus/issues/1200#issuecomment-1954929802) of the Issue to implement this feature on my blog powered by Hugo.

I added the following code to html.

```javascript
<script>
    var theme = localStorage.getItem('data-theme') == null ? 'dark' : 'light';
</script>

<div class="comments">
    <script src="https://giscus.app/client.js"
        data-repo="user/repository"
        data-repo-id="xxxxxxx"
        data-category="Comments"
        data-category-id="xxxxxx"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="dark"
        data-lang="en"
        crossorigin="anonymous"
        async>
    </script>
</div>

<script>
    document.querySelector('script[src="https://giscus.app/client.js"]').setAttribute('data-theme', theme);
</script>
```

Then I also added this script to the theme changing function of javascript.

```javascript
    const initTheme = (state) => {
        if (state === THEMES.DARK) {
            document.documentElement.classList.add(THEMES.DARK);
            document.documentElement.classList.remove(THEMES.LIGHT);
+            setGiscusTheme(THEMES.DARK);
        } else if (state === THEMES.LIGHT) {
            document.documentElement.classList.remove(THEMES.DARK);
            document.documentElement.classList.add(THEMES.LIGHT);
+            setGiscusTheme(THEMES.LIGHT);
        }
    };

+    function setGiscusTheme(theme) {
+        var iframe = document.querySelector('.giscus-frame');
+
+        if (iframe) {
+        var url = new URL(iframe.src);
+        url.searchParams.set('theme', theme);
+        iframe.src = url.toString();
+        }
+    }
```

For more details, please see [my blog theme repository](https://github.com/kktsuji/tsuji-website-theme).

## GitHub Discussions

Giscus system will store comments of this blog to the [Discussions of my blog repository](https://github.com/kktsuji/tsuji-website/discussions).
