---
applyTo: "frontend/**"
---

# Frontend Code Review Rules

These rules apply to all files under `frontend/`.

## Language: JavaScript/TypeScript

1. Use `const` by default. Only use `let` when reassignment is necessary. Never use `var`.
2. Use arrow functions for callbacks and anonymous functions.
3. All React components must be functional components (no class components).
4. Use destructuring for props.
5. All user-facing strings must be internationalized (use i18n keys, not raw strings).
6. No inline styles — use CSS modules or Tailwind classes.
7. All async operations must have error handling.
