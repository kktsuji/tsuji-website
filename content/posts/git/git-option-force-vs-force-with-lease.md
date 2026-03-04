---
title: "Git Option: --force vs --force-with-lease"
description: ""
date: 2026-03-05T07:30:00+09:00
lastmod:
draft: false
---

## Git Option: --force vs --force-with-lease

When pushing changes to a remote repository in Git, you may encounter situations where you need to overwrite existing commits. Git provides two options for this purpose: `--force` and `--force-with-lease`. Understanding the differences between these options is crucial to avoid unintended consequences.

| Feature                       | `--force` (or `-f`)                   | `--force-with-lease`                       |
| ----------------------------- | ------------------------------------- | ------------------------------------------ |
| **Overwrites remote commits** | Yes, unconditionally                  | Yes, but safely                            |
| **Checks remote state**       | No                                    | Yes, verifies remote hasn't changed        |
| **Risk of data loss**         | High - may lose others' work          | Low - prevents overwriting others' commits |
| **Use case**                  | Force push when you control the repo  | Safer default for collaborative work       |
| **Command**                   | `git push --force`                    | `git push --force-with-lease`              |
| **Requires verification**     | Manual review needed                  | Automatic safety check                     |
| **Best practice**             | Use with caution, especially in teams | Recommended for team environments          |
| **When failed**               | No failure, always push succeeds      | Push fails if remote has new commits       |

It's better to use `--force-with-lease` even if you're working on a personal branch to make it your habit.

### When to Use Each

**Use `--force`** when:

- You're working on a personal branch
- You've confirmed no one else is pushing to the branch
- You need absolute control over the push

**Use `--force-with-lease`** when:

- Working in a team environment
- You want protection against accidentally overwriting others' changes
- You need a safer force push option

## Example Scenario of `--force-with-lease` Failing

- **Person A's local branch:** `feature/new-feature` at commit `abc123`
- **Remote branch:** `feature/new-feature` at commit `abc123`
- **Person B pushes:** A new commit `def456` to remote `feature/new-feature`
- **Person A attempts:** `git push --force-with-lease`

**Result:** ❌ Push fails with error:

```bash
error: failed to push some refs to 'origin'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you are integrating with upstream changes
hint: you may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

Person A's `--force-with-lease` detects that the remote has changed since their last fetch and safely prevents the overwrite of Person B's commit `def456`.
