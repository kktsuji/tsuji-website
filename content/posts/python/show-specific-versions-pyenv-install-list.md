---
title: "Show Specific Versions with pyenv install --list"
description: ""
date: 2025-10-15T09:00:00+09:00
lastmod:
draft: false
---

## Show Specific Versions

```bash
# Show only Python 3.x versions
pyenv install -l | grep "^  3\."

# Show only Python 2.x versions
pyenv install --list | grep "^  2\."
```

- `^`: Start of the line
- `  `: Two spaces (pyenv install --list output format)
- `3\.`: Match "3." (the dot `.` means any character in regex, so escape it with `\`)
