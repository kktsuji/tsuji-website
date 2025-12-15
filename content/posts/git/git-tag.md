---
title: "Git Tag"
description: ""
date: 2025-12-16T8:00:00+09:00
lastmod:
draft: false
---

## Create a Tag

```bash
# Lightweight Tag
git tag <tagname>

# With message
git tag -a <tagname> -m "Tag message"

# With specific commit
git tag <tagname> <commit>
```

## Push Tag to Remote

```bash
# Push single tag
git push <remote> <tagname>

# Push all tags
git push <remote> --tags
```

## View Tags

```bash
# List all tags
git tag

# Show tag details
git show <tagname>
```
