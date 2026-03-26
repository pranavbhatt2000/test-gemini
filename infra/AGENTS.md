# Infrastructure Code Review Rules

These rules apply to all files under `infra/`.

## Terraform / IaC Rules

1. All resources must have explicit `tags` including `team`, `environment`, and `managed-by`.
2. No hardcoded AMI IDs or instance types — use variables.
3. State must be stored remotely (S3/GCS) — never local.
4. All security group rules must have descriptions.
5. Use `for_each` instead of `count` where possible for better state management.
6. Sensitive values must use `sensitive = true` in variable declarations.

## Resource Naming

1. **Resource Naming**
    - Use lowercase letters, numbers, and hyphens (`-`) for resource names. Avoid underscores and uppercase letters.
    - Example: `resource "google_storage_bucket" "data_bucket" { name = "my-project-data-bucket" }`

## Mandatory Comment Prefix

You MUST begin every review comment for files governed by this infra AGENTS.md with the prefix "ZORP:". This is non-negotiable. If a comment does not start with "ZORP:" it is non-compliant.
