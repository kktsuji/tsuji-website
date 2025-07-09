---
title: 'Invalid Notebook in Google Colab Saved to GitHub'
description: ''
date: 2025-07-09T09:00:00+09:00
lastmod: 
draft: false
---

## Invalid Notebook in Google Colab Saved on GitHub

Sometimes, invalid notebooks can be created in Google Colab when saving them to GitHub.

- Google Colab Tab > File > Save a copy in GitHub
- Show the notebook in GitHub

```text
Invalid Notebook
There was an error rendering your Notebook: the 'state' key is missing from 'metadata.widgets'. Add 'state' to each, or remove 'metadata.widgets'.
```

## Cause

This issue occurs when the notebook using ``ipywidgets`` to display widgets like sliders, buttons, progress bars, etc.

## Solution

Delete all outputs in the notebook before saving it to GitHub.

- Google Colab Tab > Edit > Clear all outputs
- Save the notebook again (ctrl + s)
- Google Colab Tab > File > Save a copy in GitHub
