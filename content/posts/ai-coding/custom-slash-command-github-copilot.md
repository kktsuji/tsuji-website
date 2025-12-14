---
title: "Custom Slash Commands for GitHub Copilot"
description: ""
date: 2025-12-14T10:00:00+09:00
lastmod:
math: true
draft: false
---

## Custom Slash Commands for GitHub Copilot

You can create custom slash commands for GitHub Copilot.

I analyzed how [spec-kit](https://github.com/github/spec-kit) implements custom slash commands by examining the workspace structure and configuration files.

## How to Create Custom Slash Commands for GitHub Copilot

Based on the spec-kit implementation, here's how custom slash commands work:

### Core Architecture

Custom slash commands consist of **two types of files**:

1. **Prompt files** (`.github/prompts/*.prompt.md`) - Simple triggers
2. **Agent files** (`.github/agents/*.agent.md`) - Full implementation logic

### File Structure

```text
.github/
├── prompts/
│   └── speckit.specify.prompt.md    # Simple pointer to agent
└── agents/
    └── speckit.specify.agent.md     # Full command logic
```

### 1. Prompt Files (.prompt.md)

These are minimal trigger files that reference the agent:

```markdown
---
agent: speckit.specify
---
```

That's it! The prompt file just tells Copilot which agent to invoke.

### 2. Agent Files (.agent.md)

These contain the actual command implementation with a frontmatter and instructions:

````markdown
---
description: Brief description of what this command does
handoffs:
  - label: Next Command Label
    agent: speckit.nextcommand
    prompt: Suggested user prompt
    send: true # Optional: auto-send
---

## User Input

```text
$ARGUMENTS
```
````

## Outline

[Your command's detailed instructions...]

## [Additional sections as needed]

````

**Key elements:**
- **description**: What the command does
- **handoffs**: Related commands to suggest next
- **$ARGUMENTS**: Captures text after the slash command
- **Instructions**: Detailed workflow for Copilot to follow

### 3. VS Code Settings Registration

Enable your commands in [.vscode/settings.json](.vscode/settings.json):

```json
{
    "chat.promptFilesRecommendations": {
        "speckit.specify": true,
        "speckit.plan": true,
        "yourname.mycommand": true
    }
}
````

### Naming Convention

- **File names**: `namespace.commandname.{agent|prompt}.md`
- **Example**: speckit.specify.agent.md creates `/speckit.specify` command
- The namespace (e.g., `speckit`) groups related commands

### Creating Your Own Command - Example

1. Create .github/prompts/mykit.review.prompt.md:

```markdown
---
agent: mykit.review
---
```

2. Create .github/agents/mykit.review.agent.md:

````markdown
---
description: Review code for quality and best practices
handoffs:
  - label: Fix Issues
    agent: mykit.fix
    prompt: Fix the identified issues
---

## User Input

```text
$ARGUMENTS
```
````

## Outline

1. Analyze the current file or selected code
2. Check for:
   - Code quality issues
   - Best practice violations
   - Security concerns
3. Generate a detailed report
4. Suggest improvements

````

3. Add to [.vscode/settings.json](.vscode/settings.json):
```json
{
    "chat.promptFilesRecommendations": {
        "mykit.review": true
    }
}
````

### Advanced Features

- **Scripts**: Commands can invoke bash/PowerShell scripts in `.specify/scripts/`
- **Templates**: Store reusable content in `.specify/templates/`
- **Auto-approval**: Configure trusted scripts in settings for auto-execution
- **Handoffs**: Chain commands together with suggested follow-ups

The system is very flexible - you can create simple commands with basic instructions or complex workflows with multiple phases, script execution, and file generation!### Advanced Features

- **Scripts**: Commands can invoke bash/PowerShell scripts in `.specify/scripts/`
- **Templates**: Store reusable content in `.specify/templates/`
- **Auto-approval**: Configure trusted scripts in settings for auto-execution
- **Handoffs**: Chain commands together with suggested follow-ups

The system is very flexible - you can create simple commands with basic instructions or complex workflows with multiple phases, script execution, and file generation!

## .vscode.settings.json

It's not required, but it's **highly recommended** for better user experience.

### How commands work:

Without settings.json:

- Commands still work if you type them manually (e.g., `/speckit.specify`)
- Copilot finds them from `.github/prompts/*.prompt.md` files
- No autocomplete suggestions when typing `/`

With `chat.promptFilesRecommendations`:

- ✅ Commands appear in autocomplete dropdown
- ✅ Users discover available commands easily
- ✅ Shows command descriptions
- ✅ Better IDE integration

### Best practice:

```json
{
  "chat.promptFilesRecommendations": {
    "mykit.review": true,
    "mykit.fix": true,
    "mykit.test": true
  }
}
```

When to use settings.json:

- Commands you want users to easily discover
- Team/project-specific workflows
- Commands used frequently

When to skip:

- Experimental/internal commands
- Commands you want to keep "hidden"
- Single-user temporary commands

### Alternative locations:

You can also define this in:

- User settings (settings.json) - personal commands
- Workspace settings (settings.json) - team/project commands ← Recommended for shared projects
