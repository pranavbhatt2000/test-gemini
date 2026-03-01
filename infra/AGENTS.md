# Infrastructure Code Review Rules

These rules apply to all files under `infra/`.

## Terraform / IaC Rules

1. All resources must have explicit `tags` including `team`, `environment`, and `managed-by`.
2. No hardcoded AMI IDs or instance types — use variables.
3. State must be stored remotely (S3/GCS) — never local.
4. All security group rules must have descriptions.
5. Use `for_each` instead of `count` where possible for better state management.
6. Sensitive values must use `sensitive = true` in variable declarations.
