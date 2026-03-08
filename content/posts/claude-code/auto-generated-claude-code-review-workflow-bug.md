---
title: "Auto-generated Claude Code Review Workflow Bug - No Summary Comments Generated"
description: ""
date: 2026-03-08T11:00:00+09:00
lastmod:
math: true
draft: false
---

## Issues

- Auto-generated `.github/workflows/claude-code-review.yml` for PRs review on GitHub has a bug
  - Note: `/install-github-app` command generates it in `Claude Code CLI`
- This workflow is triggered on `pull_request` events and is supposed to run the `code-review` plugin to analyze PRs and post review comments on GitHub
- However, no comments were being posted on PRs, even though the workflow runs successfully (green check)

## Solution

Use [official example](https://github.com/anthropics/claude-code-action/blob/main/docs/solutions.md) in [anthropic/claude-code-action](https://github.com/anthropics/claude-code-action?tab=readme-ov-file) instead of the auto-generated workflow.

## The Root Cause

The auto-generated `.github/workflows/claude-code-review.yml` by Claude Code CLI is just a template and is NOT fully functional out of the box. It requires manual adjustments to work correctly, especially for posting review comments on PRs.

## Example of Workflow

```yaml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize, ready_for_review, reopened]

jobs:
  review:
    # Skip forked PRs: repository secrets are not available in fork workflows
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - uses: anthropics/claude-code-action@26ec041249acb0a944c0a47b6c0c13f05dbc5b44 # v1.0.70
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          track_progress: true # Enables tracking comments
          prompt: |
            REPO: ${{ github.repository }}
            PR NUMBER: ${{ github.event.pull_request.number }}

            Please review this pull request with a focus on:
            - Code quality and best practices
            - Potential bugs or issues
            - Security implications
            - Performance considerations

            Provide detailed feedback using inline comments for specific issues.

          claude_args: |
            --allowedTools "mcp__github_inline_comment__create_inline_comment,Bash(gh pr comment:*),Bash(gh pr diff:*),Bash(gh pr view:*)"
```

## Results

Tracking comment while running the workflow:

![img](https://img.tsuji.tech/auto-generated-claude-code-review-workflow-bug-0.jpg)

Review comment posted on GitHub PR after workflow completion:

![img](https://img.tsuji.tech/auto-generated-claude-code-review-workflow-bug-1.jpg)

## claude.yml Does Not Need Manual Adjustments

Actually, the `/install-github-app` command in Claude Code CLI generates two files:

- `.github/workflows/claude-code-review.yml` for PR review (which has the bug)
- `.github/workflows/claude.yml` for general automation when `@claude` is mentioned in a comment (which works fine without adjustments)

First one has a bug and requires manual adjustments, while the second one works correctly like the below image without any adjustments:

![img](https://img.tsuji.tech/auto-generated-claude-code-review-workflow-bug-2.jpg)
