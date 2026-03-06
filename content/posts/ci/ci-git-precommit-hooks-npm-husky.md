---
title: "CI using Git pre-commit hooks with npm and husky"
description: ""
date: 2026-03-04T8:00:00+09:00
lastmod:
math: false
draft: false
---

## CI using Git pre-commit hooks with npm and husky

- [Git pre-commit hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) allow you to run scripts before a commit is made, which can be useful for running tests, linters, or other checks to ensure code quality. [npm husky](https://typicode.github.io/husky/#/) is a popular tool that makes it easy to manage Git hooks in JavaScript projects.

## Install npm via fnm

For more details, see [fnm - Fast and simple Node.js version manager](https://github.com/Schniz/fnm).

```bash
sudo apt install -y curl unzip

curl -fsSL https://fnm.vercel.app/install | bash

fnm --version
```

Install latest stable Node.js:

```bash
# Install latest stable Node.js
fnm install --lts


# Use it (current shell session only)
fnm use --lts

# Set as default (default for all shell sessions)
fnm default lts-latest

# Confirm
node --version
npm --version
```

## Set up Project

After setting up the project, whenever you try to commit changes, the pre-commit hook will run `npm test` before allowing the commit to proceed. You can replace `npm test` with any command you want to run as part of your pre-commit checks.

### Initialize npm project and install husky

If you haven't already set up a project, you can do so with the following commands:

```bash
cd your-project

# Initialize npm project
npm init -y

# Install husky
npm install husky --save-dev

# Initialize husky (creates .husky/pre-commit and adds prepare script)
npx husky init

# Edit .husky/pre-commit to add your hook command
echo "npm test" >> .husky/pre-commit
```

And add the test script manually to `package.json`:

```json
"scripts": {
  "prepare": "husky",
  "test": "echo \"Running tests...\" && exit 0"
}
```

### Set up the existing settings

If the project already has a `package.json` with husky configured, you can simply run:

```bash
# Install dependencies
npm install
```
