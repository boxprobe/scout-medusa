---
name: api-keys.publishable-api-keys-crud
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
3. Enter admin credentials in the password field
4. Click "Continue with Email" button to log in
5. Navigate to the publishable API keys settings page
6. Click "Create" button to start creating a new API key
7. Enter a unique name in the title input field
8. Click "Save" button to create the API key
9. Click "Publishable API Keys" link to return to the main API keys page
10. Search for the created API key using its title
11. Click the edit menu for the found API key
12. Click "Edit" button to modify the API key
13. Enter a new unique name in the title input field
14. Click "Save" button to update the API key
15. Click the edit menu again
16. Click "Revoke API key" to revoke the API key
17. Confirm revocation by clicking "Revoke API key" button
18. Click the delete menu
19. Click "Delete" to delete the API key
20. Confirm deletion by clicking "Delete" button
21. Verify the API key has been removed and page shows "Publishable API Keys" heading

## Assertions

- **url_match**: Verify navigation to publishable API keys settings page
- **element_visible**: Verify the main heading is visible after deletion
- **text_content**: Verify the page displays "Publishable API Keys" heading, confirming successful deletion
