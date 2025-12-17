---
description: Translation Command
argument-hint: "#file:articles.md (the English or Japanese file to be translated)"
---

# Translation Command

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding.

## Command Usage

`/kktsuji.translate #file:article.md`

Takes one article file as an argument. The content should be in either English or Japanese.

## Outline

1. **Read the file content** from the provided file argument
   - **⚠️ IMPORTANT: Argument Validation**
   - If `$ARGUMENTS` is empty or no file is provided:
     1. Display a warning message: "❌ Error: No file specified. Please provide a file to translate using `#file:article.md`"
     2. Stop processing immediately
     3. Do not proceed with any translation
2. **Detect the language**: Determine if the article is written in English or Japanese
   - **⚠️ Language Validation**: If the content is neither English nor Japanese:
     1. Display a warning message: "❌ Error: Unsupported language detected. This command only supports English and Japanese content."
     2. Stop processing immediately
     3. Do not proceed with any translation
3. **Translate the content**:
   - If English → Translate to Japanese
   - If Japanese → Translate to English
4. **Overwrite the file** with the translated content

## Translation Constraints (English to Japanese)

When translating from English to Japanese, follow these rules:

- **No space between Japanese and English text** (Example: これはtestです。)
- **No space between Japanese and half-width numbers** (Example: これは123です。)
- **No space between Japanese and half-width symbols** (Example: これは"test"です。)
- **Preserve spaces between English words** (Example: AWS Lambda)
- **Keep well-known terms and technical terms in English** (Examples: Deep Learning, AWS, DDPM, PyTorch, etc.)
- **No space between English and Markdown syntax** (Example: これは`test`です。)
- **In Markdown code blocks**: Translate comments and prompts to Japanese, but keep code syntax unchanged

## Translation Constraints (Japanese to English)

To be determined.
