# Social-posts

Experiments around social-post workflows and backend CRUD patterns.

## Repository layout

- `backend-sqlalchemy-CRUD-routes/` contains the current SQLAlchemy CRUD-route work.

## Development notes

Keep API changes isolated from experiments, document new endpoints, and never commit database credentials or local environment files.

## Before opening a change

- Reproduce the issue or describe the intended behavior.
- Verify the affected route or workflow locally.
- Keep commits focused and avoid unrelated generated files.

## Local environment

Keep secrets and machine-specific settings outside version control. For local configuration, use environment variables or an untracked `.env` file and provide safe example values in documentation when a new setting is required.

A typical local setup can use placeholder values such as:

```text
DATABASE_URL=postgresql://user:password@localhost:5432/example_db
```

Replace the placeholder credentials locally and keep the real values out of Git.
