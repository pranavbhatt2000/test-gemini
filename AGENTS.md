# Repository-Wide Code Review Rules

These rules apply to ALL files in this repository regardless of language or directory.

## General Rules

1. All functions must have docstrings or comments explaining their purpose.
2. No hardcoded secrets, API keys, or credentials anywhere in the codebase.
3. Unused imports must be removed.
4. Unused variables must be removed.
5. All error handling must be explicit — no bare `except:` or empty `catch` blocks.
6. Magic numbers must be replaced with named constants.
7. File names must use snake_case (Python) or camelCase (Go/JS/Rust).
8. Every public function must have at least one unit test.

## PR Etiquette

- PR titles must be descriptive (not "fix stuff" or "updates").
- PRs should not exceed 500 lines of changes unless justified.

## Mandatory Comment Prefix

You MUST begin every review comment for files governed by this root AGENTS.md with the prefix "ALPHA:". This is non-negotiable. If a comment does not start with "ALPHA:" it is non-compliant.
