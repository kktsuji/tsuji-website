---
title: 'Fix Required Status Check Deadlock with a paths-ignore Skip Workflow in GitHub Actions'
description: ""
date: 2026-03-07T16:00:00+09:00
lastmod:
draft: false
---

## Deadlock Situation

### Branch Protection

- Status check: `unit-tests` (required)

### GitHub Actions Workflow

A workflow `.github/workflows/tests.yml` only runs when `src/` or `tests/` are modified.

```yaml
name: Tests

on:
  pull_request:
    branches: [main]
    # Only run when source code or test code is modified
    paths:
      - "src/**"
      - "tests/**"

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      # Run tests
...
```

### Pull Request

- `src/` and `tests/` are **NOT** modified.

### Result

- Status check `unit-tests` is **NOT** triggered.
- Pull request cannot be merged because the required status check `unit-tests` is not successful.
- Pull request is in a deadlock.

## Solution

### Create a Skip Workflow

Create `.github/workflows/tests-skip.yml` with `paths-ignore` option.

```yaml
name: Tests (skip)

on:
  pull_request:
    branches: [main]
    # Run when changes are made "outside" of source code and tests
    paths-ignore:
      - "src/**"
      - "tests/**"

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      # Just echo a message (no tests are run)
      - run: echo "No source changes — skipping tests"
```

### Result with Skip Workflow

- When `src/` and `tests/` are **NOT** modified, the skip workflow is triggered, and the status check `unit-tests` is successful.
- Pull request can be merged.
- No deadlock occurs.
