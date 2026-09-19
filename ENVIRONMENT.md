# Local Environment Guide

Keep local configuration outside version control and document required settings with safe placeholders.

## Rules

- Store real credentials only in local environment variables or an untracked `.env` file.
- Never commit production credentials, tokens, or private connection strings.
- Use placeholder values in documentation and examples.
- If a credential is exposed, revoke or rotate it before cleaning the repository history.

## Database example

```text
DATABASE_URL=postgresql://user:password@localhost:5432/example_db
```

The example above is documentation only. Replace it with local values when running the application.

## Adding a new setting

When a new environment variable is required, document its name, purpose, whether it is required, and a safe example value. Avoid documenting real secrets or personal configuration.