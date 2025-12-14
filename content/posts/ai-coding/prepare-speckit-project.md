---
title: "Prepare Spec Kit Project for Specification-Driven AI Coding"
description: ""
date: 2025-12-14T10:00:00+09:00
lastmod:
math: true
draft: false
---

## Prepare Speckit Project for Specification-Driven AI Coding

To use specification-driven AI coding with Spec Kit, you need to set up a Spec Kit project. Follow these steps to prepare your project environment.

Creating a New Project:

```bash
mkdir your-project
cd your-project
```

Create Python Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer):

```bash
pip install -U pip
pip install uv
```

Install [Spec Kit](https://github.com/github/spec-kit) via uv:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

(Optional) Update Shell Configuration:

```bash
uv tool update-shell
source ~/.bashrc
source venv/bin/activate
```

Initialize Spec Kit Project:

```bash
specify init --here
```
