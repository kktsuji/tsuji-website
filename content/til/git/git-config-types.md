---
title: 'Types of Git Config'
description: ''
date: 2024-11-09T12:00:00+09:00
lastmod: 
draft: false
---

Three types of git config:

| Option     | File Location                    | Description                    |
| ---------- | -------------------------------- | ------------------------------ |
| `--system` | `/etc/gitconfig`                 | For whole system (all users)   |
| `--global` | `~/.gitconfig`                   | For all repositories of a user |
| `--local`  | `project_folder/.git/.gitconfig` | For a repository               |

Git loads configs in order `--system`, `--global`, `--local`. Settings loaded later have priority.

Print setting list:

```bash
# All settings
git config -l

# Global settings
git config --global -l
```

Usage:

```bash
git config
```


Reference:

- [Customizing Git - Git Configuration - git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
