---
applyTo: "backend/auth/**"
---

# Auth Module Review Rules

These rules apply to all files under `backend/auth/`.

## Security-Critical Module

This module handles authentication and authorization. Extra scrutiny required.

1. NEVER log sensitive data (passwords, tokens, session IDs).
2. All password comparisons must use constant-time comparison functions.
3. Tokens must have expiration times — no indefinite tokens.
4. Rate limiting must be implemented on all auth endpoints.
5. Failed auth attempts must be logged with IP address and timestamp.
6. All auth functions must have explicit return types annotated.
