---
title: "Custom Slash Command Definition in Prompt Files for GitHub Copilot"
description: ""
date: 2025-12-26T08:00:00+09:00
lastmod:
math: true
draft: false
---

## Prompts Files for GitHub Copilot

GitHub Copilot allows you to create [prompt files](https://code.visualstudio.com/docs/copilot/customization/prompt-files) that can create custom prompts to enhance your experience.

## How to Create Prompt Files for GitHub Copilot

Manual:

1. Create a new file `namespace.prompt-name.prompt.md` in the `.github/prompts/` directory of your repository.
2. Define the prompt's behavior using frontmatter and instructions in the file.

GUI:

1. Open the GitHub Copilot chat sidebar in Visual Studio Code.
2. Click on the "Create New Prompt" in setting gear icon (at the top of the chat sidebar).
3. Define the prompt's name, description, and behavior using the provided interface.

## VSCode Settings for Prompt Files

You can configure `.vscode/settings.json` to set SUGGESTED ACTIONS for prompt files as follows:

```json
{
  "chat.promptFilesRecommendations": {
    "namespace.prompt-name": true
  }
}
```

The prompt files listed under `chat.promptFilesRecommendations` will appear as suggested actions in the GitHub Copilot chat sidebar.

## Example of a Prompt File Definition

```markdown
---
description: Translate text from English to French.
name: namespace.prompt-name
argument-hint: Text in English to be translated into French.
agent: agent # You can also specify a custom agent here
model: gpt-5
tools: ["file_search"]
---

# Instructions for the prompt

You are a professional translator. Translate the following English text into French while maintaining the original meaning and tone.
...
```

See the [official documentation](https://code.visualstudio.com/docs/copilot/customization/prompt-files) for more details on creating and configuring prompt files for GitHub Copilot.

## How to Use Prompt Files

1. Open the GitHub Copilot chat sidebar in Visual Studio Code.
2. input the prompt name with a slash (e.g., `/namespace.prompt-name`) in the chat input box.
3. Provide any required arguments if prompted, and interact with the prompt as needed.

## Prompt Files vs. Custom Agents

| Feature     | [Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files) | [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) |
| ----------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Purpose     | Simple triggers to invoke agents                                                      | Full implementation logic for complex tasks                                             |
| File Type   | `.prompt.md` files                                                                    | `.agent.md` files                                                                       |
| Complexity  | Minimal frontmatter, just points to an agent                                          | Detailed frontmatter with tools, handoffs, and instructions                             |
| Use Cases   | Quick commands, simple tasks                                                          | Comprehensive workflows, multi-step processes                                           |
| Persistence | Just one response per invocation                                                      | Can maintain context over multiple interactions in a session                            |

File Structure:

```text
.github/
├── agents/
│   └── namespace.agent-name.agent.md     # Custom agent
└── prompts/
    └── namespace.prompt-name.prompt.md    # Prompt file
```
