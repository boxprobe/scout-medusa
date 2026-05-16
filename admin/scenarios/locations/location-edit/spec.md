---
name: locations.location-edit
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
5. Navigate to the locations settings page
6. Click "Create" button to start creating a new location
7. Enter a unique name in the name-input field
8. Enter a unique name in the address-input field
9. Click the country-list button to select a country
10. Select "Albania" from the country dropdown
11. Click "Save" button to create the location
12. Click the edit-menu button for the created location
13. Click "Edit" button to edit the location
14. Enter a unique number in the post-code-input field
15. Click "Save" button to save the changes
16. Click "Locations" link to return to the locations list
17. Search for the created location using the search-text field
18. Click the edit-menu-2 button for the found location
19. Click "Delete" button to delete the location
20. Click "Remove" button to confirm deletion
21. Verify that "No records" message is displayed

## Assertions

- **url_match**: Verifies navigation to the locations settings page
- **text_matched**: Confirms successful creation, editing, and deletion actions
- **text_content**: Validates that the location is successfully deleted by checking for "No records" message
