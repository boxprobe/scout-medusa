---
name: auth.protected-routes-redirect-unauthenticated-users
url: /app/login
tags:
- smoke
- core
- navigation
priority: critical
---

## Preconditions

- logged_in: False
- page: /app/login

## Steps

1. Navigate to the orders page at /orders
2. Navigate to the products page at /products  
3. Navigate to the store settings page at /settings/store

## Assertions

- **url_match**: Verify that accessing /orders redirects to /login page
- **url_match**: Verify that accessing /products redirects to /login page
- **url_match**: Verify that accessing /settings/store redirects to /login page
