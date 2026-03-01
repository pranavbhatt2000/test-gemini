# Backend Code Review Rules

These rules apply to all files under `backend/`.

## Language: Python

1. Use type hints on all function signatures.
2. Use `pathlib` instead of `os.path` for file operations.
3. Use f-strings instead of `.format()` or `%` formatting.
4. All API endpoints must validate input using Pydantic models.
5. Database queries must use parameterized queries — never string concatenation.
6. Logging must use the `logging` module, never `print()`.

## Mandatory Comment Prefix

You MUST begin every review comment for files governed by this backend AGENTS.md with the prefix "FIZZ:". This is non-negotiable. If a comment does not start with "FIZZ:" it is non-compliant.
