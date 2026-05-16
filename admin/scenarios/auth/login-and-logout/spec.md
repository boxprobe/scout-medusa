---
name: auth.login-and-logout
url: /app/orders
tags:
- smoke
- core
- navigation
priority: critical
---

## Preconditions

- logged_in: False
- page: /login

## Steps

1. Navigate to the login page
2. Enter admin credentials in the email field
3. Enter admin credentials in the password field
4. Click "Continue with Email" button to submit login form
5. Click on the user profile button (admin@medusa-test.com) in the settings
6. Click "Log out" to end the session

## Assertions

- **url_match**: User is redirected to /orders page after successful login
- **url_match**: User is redirected back to /login page after logging out
