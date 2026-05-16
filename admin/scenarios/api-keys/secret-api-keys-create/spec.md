---
name: api-keys.secret-api-keys-create
url: /login
tags:
- core
- crud
priority: medium
---

## Preconditions

- logged_in: False
- page: /login

## Steps

1. Navigate to the login page
2. Enter admin credentials in the email field
3. Enter admin password in the password field
4. Click "Continue with Email" button to log in
5. Navigate to the secret API keys settings page
6. Click the "Create" button to start creating a new API key
7. Enter a unique name in the title input field
8. Click "Save" button to create the API key
9. Click "Continue" button in the token dialog to proceed
10. Verify the created API key appears in the list with the correct title
11. Click the delete menu for one API key
12. Click "Revoke API key" option from the menu
13. Confirm the revocation by clicking "Revoke API key" button
14. Verify the API key status shows as "Revoked"
15. Click the edit menu for another API key
16. Click "Delete" option from the menu
17. Confirm the deletion by clicking "Delete" button
18. Return to the Secret API Keys main page

## Assertions

- **url_match**: Settings page loads correctly at /settings/secret-api-keys
- **text_matched**: Create button is clickable and responsive
- **text_content**: Created API key displays with the correct unique name
- **text_matched**: Revoked API key shows "Revoked" status
- **text_matched**: Navigation returns to "Secret API Keys" page after operations
