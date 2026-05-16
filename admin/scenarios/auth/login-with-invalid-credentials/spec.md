---
name: auth.login-with-invalid-credentials
url: /app/login
tags:
- core
- smoke
priority: critical
---

## Preconditions

- logged_in: False
- page: /login

## Steps

1. Navigate to the login page at /login
2. Enter invalid email "invalide@email.com" in the email input field
3. Enter invalid password "invalid-password" in the password input field
4. Click the "Continue with Email" button

## Assertions

- **url_match**: User remains on the login page (/login) after attempting login with invalid credentials
