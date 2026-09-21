# API error-handling guide

Keep API failures predictable for clients and useful for debugging.

## Recommended response shape

Return a stable error object with:

- `status`: HTTP status code or a stable application status identifier.
- `code`: machine-readable error code.
- `message`: short, user-safe description.
- `details`: optional structured context that does not expose secrets.

## Server-side rules

- Validate request input before performing writes.
- Use appropriate HTTP status codes instead of returning `200` for failures.
- Log diagnostic details server-side, but never log passwords, tokens, cookies, or authorization headers.
- Keep error codes stable so frontend code does not need to parse human-readable messages.

## Client-side rules

Show actionable messages to users and handle unexpected responses with a safe generic fallback. Do not display raw stack traces or server internals in the UI.