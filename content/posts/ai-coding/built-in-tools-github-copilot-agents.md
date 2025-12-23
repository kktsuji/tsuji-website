---
title: "Built-in Tools in GitHub Copilot Agents"
description: ""
date: 2025-12-23T8:00:00+09:00
lastmod:
math: true
draft: false
---

## Built-in Tools in GitHub Copilot Agents

GitHub Copilot Agents support the use of [Built-in tools](https://code.visualstudio.com/docs/copilot/chat/chat-tools) that can enhance the capabilities of them.

## Configure Tools (GUI)

You can configure which built-in tools are enabled for AI agents in the GitHub Copilot settings in Visual Studio Code.

1. Open chat sidebar in VS Code
2. Select the agent you want to configure (from the dropdown at the bottom left of the chat input box)
3. Click on the tool icon next to the agent name (at the bottom of the chat input box)
4. In the "Configure Tools" dialog, you can enable or disable specific tools for the selected agent.

## Custom Agents Settings

When defining a [custom agent](https://code.visualstudio.com/docs/copilot/customization/custom-agents), you can specify which built-in tools the agent is allowed to use by including the `tools` section in the agent definition file (`.agent.md`).

```markdown
---
description: aaa
tools: ["create_directory", "create_file"] # List of built-in tools the agent can use
handoffs:
  - label: xxx
    agent: yyy
    prompt: zzz
    send: false
---
```

## List Command

You can confirm the list of available tools for agents using `/list` command in the chat.

Prompt:

```text
/list
```

Response:

```markdown
Available tools:

- create_directory
- create_file
- create_new_jupyter_notebook
- create_new_workspace
- edit_notebook_file
- fetch_webpage
- file_search
- grep_search
- get_changed_files
- get_errors
- copilot_getNotebookSummary
  ...
```

You cannot execute these tools directly in the chat. Instead, the AI agents automatically decide when to use them internally based on the context of the natural language requests in chat.

For example:

- You say: "read the config file" → AI uses `read_file` tool
- You say: "find all uses of the login function" → AI uses `list_code_usages` or `grep_search`
- You say: "run the tests" → AI uses `run_in_terminal`

If you want to know the description of each tool, you can refer to the [official documentation](https://code.visualstudio.com/docs/copilot/chat/chat-tools) or ask the agent:

Prompt:

```markdown
Please list and describe the available built-in tools you can use.
```

Response:

```markdown
## File Operations

- create_file - Create new files with content
- read_file - Read file contents with line range specification
- replace_string_in_file - Edit files by replacing exact string matches
- multi_replace_string_in_file - Perform multiple file edits in one operation
- list_dir - List directory contents
- create_directory - Create directory structures
  ...
```

## Chat Debug View

You can also see the details of them in the `Chat Debug View` in VS Code (see [my previous post](https://tsuji.tech/chat-debug-view-github-copilot/)).

- Which tool was used by the agent
- Input parameters passed to the tool
- Output results returned from the tool
- etc.
