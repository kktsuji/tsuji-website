---
title: "Gitflow vs. Trunk-based Development"
description: ""
date: 2026-02-17T18:00:00+09:00
lastmod:
draft: false
---

## Summary

|                       | Gitflow                                                                        | Trunk-based Development                                                                   |
| --------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Branching Model       | main, develop, feature, release, hotfix                                        | Single main branch (trunk) and short-lived feature branches                               |
| Integration Frequency | Less frequent, often at the end of a feature or release                        | Continuous integration, multiple times a day                                              |
| Complexity            | Higher due to multiple branches and merging                                    | Lower due to fewer branches and simpler merging                                           |
| Release Process       | Can be more complex with multiple branches                                     | Simpler with a single branch                                                              |
| Collaboration         | Can lead to longer-lived branches and potential merge conflicts                | Encourages frequent collaboration and integration, reducing merge conflicts               |
| Use Cases             | Suitable for larger teams and projects with well-defined release cycles        | Suitable for smaller teams and projects that require rapid development and deployment     |
| Pros.                 | Clear separation of development stages, easier to manage releases              | Faster development cycles, reduced merge conflicts, encourages continuous integration     |
| Cons.                 | Can lead to merge conflicts, slower development cycles, more complex branching | Can be challenging for larger teams, requires discipline to maintain short-lived branches |

## Gitflow

Gitflow is a branching model for Git, created by Vincent Driessen. It defines a strict branching strategy designed around the project release. The main branches in Gitflow are:

- `main`: The main branch that always reflects a production-ready state.
- `develop`: The branch where the latest development changes are integrated. It serves as an integration branch for features.
- `feature/*`: Branches created from `develop` for developing new features. Once a feature is complete, it is merged back into `develop`.
- `release/*`: Branches created from `develop` when preparing for a new release. They allow for final bug fixes and preparing release notes. Once ready, they are merged into both `main` and `develop`.
- `hotfix/*`: Branches created from `main` to quickly address critical issues in production. Once the hotfix is complete, it is merged back into both `main` and `develop`.

## Trunk-based Development

Trunk-based development is a software development practice where all developers work on a single branch, often called "trunk" or "main". In this model, developers create short-lived feature branches that are merged back into the trunk frequently, often multiple times a day. The key principles of trunk-based development include:

- **Single Branch**: All development happens on a single branch, reducing the complexity of managing multiple branches.
- **Continuous Integration**: Developers integrate their changes into the trunk frequently, which helps to identify and resolve conflicts early.
- **Short-lived Feature Branches**: If feature branches are used, they are short-lived and merged back into the trunk as soon as possible to minimize divergence.
- **Automated Testing**: Continuous integration is often paired with automated testing to ensure that changes do not break the build or introduce bugs.
- **Release Process**: Releases are typically made from the trunk, and feature flags may be used to control the visibility of new features until they are ready for production.
