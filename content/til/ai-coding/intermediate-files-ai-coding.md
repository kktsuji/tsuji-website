---
title: "Intermediate Files Improve AI Coding Performance"
description: ""
date: 2025-12-13T8:00:00+09:00
lastmod:
math: true
draft: false
---

## Intermediate Files Improve AI Coding Performance

With difficult orders, AI agents like GitHub Copilot may struggle to complete tasks effectively. They sometimes forget important context or make mistakes. To help with this, you can use `intermediate files` to break down complex tasks into smaller, manageable parts.

For example, this prompt is **too complex**:

```text
I want to change the specifications in this project.

Before: XXX
After: YYY

Please update all relevant source code files to reflect these changes.
```

Instead, you can break it down into some steps and create intermediate files for each steps.

Key points:

1. Break down the task
2. Create intermediate files in each step
3. Execute step by step by using the intermediate files created in the previous step

Merits:

- Smaller tasks are easier for AI to handle.
- Intermediate files help retain context and instructions.
- TODO lists make it clear what needs to be done.
- You can review and verify each step before moving on.

## 1. Break Down into Steps

First, divide the complex task into smaller steps.

For example:

1. Investigate which parts of the code need to be changed.
2. Create a executable todo list of changes.
3. Implement the changes based on the todo list.
4. Check and test the changes.

## 2. Create Intermediate Files in Each Step

For each step, create an intermediate file that contains the necessary information or instructions for that step.

For example:

### Step 1: Investigate Changes

```text
I want to change the specifications in this project.

Before: XXX
After: YYY

Please analyze the `src/aaa/*.py` files and summarize which parts of the code need to be changed to reflect these new specifications.
And save the summary in `docs/change_summary.md`.
```

### Step 2: Create a TODO List

```text
Based on the analysis in `docs/change_summary.md`, please create an executable TODO list of changes that need to be made to the source code files.
Save the TODO list in `docs/change_todo.md`.
```

Note: Instead of creating the new todo file, adding the todo list to the existing summary file as the new section is also nice.

### Step 3: Implement Changes

```text
Please implement the changes following the todo list in `docs/change_todo.md`.
After completing the changes, please mark each item in the todo list as done.
```

### Step 4: Check and Test Changes

```text
`docs/change_todo.md` is the todo list with completed changes marked.
Please confirm that all changes have been made correctly.
Also, run tests to ensure everything works as expected.
```

Note: It is better to use the AI agents for reviewing and testing rather than doing it manually.

### Step 5: Review Manually

Finally, review the changes and test results manually to ensure everything is correct.
