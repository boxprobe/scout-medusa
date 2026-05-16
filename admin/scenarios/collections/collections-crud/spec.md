---
name: collections.collections-crud
url: /login
tags:
- core
- crud
priority: high
---

## Preconditions

- logged_in: False
- page: /login

## Steps

1. Navigate to the login page
2. Enter admin credentials in the email field
3. Enter admin password in the password field
4. Click the "Continue with Email" button to log in
5. Navigate to the collections page
6. Click the "Create" button to start creating a new collection
7. Enter a unique name in the title-input field
8. Enter the same unique name in the handle-input field
9. Click the "Create" button to save the new collection
10. Verify the collection appears with the correct title
11. Click the edit-menu button to access collection options
12. Click the "Edit" button to modify the collection
13. Enter a new unique name in the new-title-input field
14. Click the "Save" button to update the collection
15. Verify the collection title has been updated
16. Click the edit-menu button again to access delete options
17. Click the "Delete" button to initiate deletion
18. Click the "Confirm" button to confirm deletion
19. Verify return to the collections page

## Assertions

- **url_match**: Collections page loads correctly after login
- **text_matched**: Create button is functional and responsive
- **text_matched**: Collection creation is successful
- **text_content**: New collection displays with the correct title
- **text_content**: Collection title updates correctly after editing
- **text_matched**: Successfully returns to collections page after deletion
