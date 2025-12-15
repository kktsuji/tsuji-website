---
title: "Standard Docs for Spec Kit Reduce Conflicts of Specifications in Each Feature"
description: ""
date: 2025-12-15T8:00:00+09:00
lastmod:
math: true
draft: false
---

## Standard Docs for Spec Kit

[Spec Kit](https://github.com/github/spec-kit) is a useful tool for the specification-driven development powered by AI.

However, the parallel development by some members with Spec Kit may lead to conflicts of detailed specifications over features. To address this, to prepare standard documentation for the project is one of better solutions.

1. Prepare standard documentations
2. Use Spec Kit with the prompts clearly indicating the standard documents

## Preparing Standard Documents

It is important to define the rules and guidelines which the project members should follow. The examples of standard documents include:

```text
docs/
├── README.md   # Entry point for standard documents
├── architecture.md
├── coding-standards.md
├── api-specifications.md
├── data-models.md
├── database-schema.md
├── testing-guidelines.md
└── etc.
```

Note:

- You don't need to prepare the perfect documents at the beginning. You can iteratively improve them as the project progresses.
- `README.md` is recommended to provide an overview of the project and link to other standard documents.

## Using Spec Kit with Standard Documents

When using Spec Kit, make sure to include references to the standard documents in your prompts. For example:

```text
/speckit.specify
Users can create an account by providing a username, email, and password.

**MUST**: Follow the standard documentation provided in `docs/README.md`.
```
