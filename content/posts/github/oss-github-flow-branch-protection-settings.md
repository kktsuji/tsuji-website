---
title: "Branch Protection Settings for GitHub Flow in Small Open Source Projects"
description: ""
date: 2026-03-03T09:00:00+09:00
lastmod:
draft: false
---

## Prerequisites

- OSS Repository on GitHub
- Admin permissions for the repository
- Use GitHub Flow workflow
  - Default branch is `main`
  - Feature branches are created from the default branch and merged back to the default branch via pull requests
  - Pull requests are used for code review, Continuous integration (CI) checks and collaboration before merging changes to the default branch

## What I Want to Achieve

- Nobody can push directly to the default branch. All changes must go through pull requests.
- CI checks must pass before merging pull requests
- Copilot auto-added to pull request reviews to assist code review and maintain code quality
- All conversations must be resolved before merging pull requests
- Pull requests are merged using `Squash and merge` or `Rebase and merge` to maintain a clean commit history
- Delete branches after pull requests are merged automatically to keep the repository clean and organized

## GitHub Repository Settings

### General Settings

Go to GitHub repository > Settings > General

- Set `Default branch` to `main`
- Disable `Allow merge commits` to prevent merge commits in the default branch and maintain a cleaner commit history
- Enable `Allow squash merging`, which helps maintain a cleaner commit history by combining all commits from a feature branch into a single commit
  - Set `Pull request title and description` in `Allow squash merging`, which provides context for the changes being merged
- Enable `Allow rebase merging`, which helps maintain a cleaner commit history by rebasing commits from a feature branch onto the default branch before merging
- Disable `Allow auto-merge` to prevent pull requests from being merged automatically without passing CI checks and code review
- Enable `Automatically delete head branches` to automatically delete feature branches after pull requests are merged, keeping the repository clean and organized

### Rules Settings

Go to GitHub repository > Settings > Rules > New ruleset

- Set `<Ruleset name>` to `Ruleset name`
- Set `Active` to `Enforcement status`
- Set `Default branch` to `Target branches`
- Enable `Require a pull request before merging` to ensure that all changes to the default branch go through pull requests, which allows for code review and CI checks before merging
  - Enable `Require conversation resolution before merging`, which helps maintain code quality and ensures that all feedback is addressed
  - Disable `Merge` and Enable `Squash` and `Rebase` to `Allowed merge methods`, which helps maintain a cleaner commit history by preventing merge commits and allowing only squash and rebase merges
- Enable `Require status checks to pass` to ensure that all CI checks pass before merging pull requests, which helps maintain code quality and prevents broken code from being merged into the default branch
  - Add your CI actions to `Status checks that are required`, which ensures that the specific CI checks you have set up are required to pass before merging pull requests
- Enable `Block force pushes` to prevent force pushes to the default branch, which can overwrite commit history and cause issues for collaborators
- Enable `Automatically request Copilot code review`, assisting with code review and maintaining code quality
