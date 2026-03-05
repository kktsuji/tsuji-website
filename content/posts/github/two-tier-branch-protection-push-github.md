---
title: 'Two-tier branch protection: managing who can push in GitHub'
description: ""
date: 2026-03-05T08:00:00+09:00
lastmod:
draft: false
---

## Two-tier branch protection: managing who can push in GitHub

While owners and collaborators are the only ones who _could_ push directly, they are often **restricted by rules** to ensure code quality and security. If you try to push and get an error saying "protected branch," it means the project requires a PR regardless of your rank.

## 1. Access Roles (Who has the "Permission"?)

To push anything to a repository, you must first have **Write Access**.

- **Repository Owners:** Have full control by default.
- **Collaborators:** Can push directly **if** they have been granted "Write" or "Admin" permissions.

## 2. Branch Protection (Why even Owners/Collaborators might be blocked)

In professional projects, the `main` or `develop` branches are usually "protected." If **Branch Protection Rules** are active:

- **Direct Push is Disabled:** Even if you are the owner, GitHub will reject a direct push.
- **PR Requirement:** You are forced to create a Pull Request, pass automated tests, and often get a peer review before the code can be merged.

### Summary Table

| Scenario                    | Who can push directly?   | Note                                 |
| --------------------------- | ------------------------ | ------------------------------------ |
| **No Protection**           | Anyone with Write access | Fast, but risky for production code. |
| **Protected Branch**        | **Nobody** (usually)     | Everyone must use a Pull Request.    |
| **Protected w/ Exceptions** | Admins / Specific users  | Rules can be set to allow "Bypass."  |
