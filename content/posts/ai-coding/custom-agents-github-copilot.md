---
title: "Custom Agents for GitHub Copilot"
description: ""
date: 2025-12-25T10:00:00+09:00
lastmod:
math: true
draft: false
---

## Custom Agents for GitHub Copilot

GitHub Copilot allows you to create [custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) that can perform specific tasks based on your requirements.

## How to Create Custom Agents for GitHub Copilot

Manual:

1. Create a new file `namespace.angent-name.agent.md` in the `.github/agents/` directory of your repository.
2. Define the agent's behavior using frontmatter and instructions in the file.

GUI:

1. Open the GitHub Copilot chat sidebar in Visual Studio Code.
2. Click on the "Create New Agent" button in the agent selection dropdown (at the bottom left of the chat input box).
3. Define the agent's name, description, and behavior using the provided interface.

## Example of a Custom Agent Definition

```markdown
---
description: This agent helps with code reviews by providing suggestions and improvements.
tools: ["file_search", "fetch_webpage"] # List of built-in tools the agent can use
handoffs:
model: Claude Sonnet 4.5
- label: Suggest Improvements
  agent: agent
  prompt: "Please suggest improvements for the following code:"
---

# Instructions for the agent

You are a professional code reviewer. Analyze the provided code and suggest improvements, optimizations, and best practices.

...
```

See the [official documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents) for more details on creating and configuring custom agents for GitHub Copilot.

## How to Use Custom Agents

1. Open the GitHub Copilot chat sidebar in Visual Studio Code.
2. Select your custom agent from the agent selection dropdown (at the bottom left of the chat input box).
3. Interact with the agent by typing prompts or commands in the chat input box.

## Custom Prompts vs. Custom Agents

| Feature     | [Custom Prompts](https://code.visualstudio.com/docs/copilot/customization/prompt-files) | [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) |
| ----------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Purpose     | Simple triggers to invoke agents                                                        | Full implementation logic for complex tasks                                             |
| File Type   | `.prompt.md` files                                                                      | `.agent.md` files                                                                       |
| Complexity  | Minimal frontmatter, just points to an agent                                            | Detailed frontmatter with tools, handoffs, and instructions                             |
| Use Cases   | Quick commands, simple tasks                                                            | Comprehensive workflows, multi-step processes                                           |
| Persistence | Just one response per invocation                                                        | Can maintain context over multiple interactions in a session                            |

File Structure:

```text
.github/
├── agents/
│   └── speckit.specify.agent.md     # Custom agent
└── prompts/
    └── speckit.specify.prompt.md    # Custom prompt
```
