---
name: categories.categories-crud
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
3. Enter admin credentials in the password field
4. Click "Continue with Email" button to log in
5. Navigate to the categories page
6. Verify the Categories page loads with the correct title
7. Click the "Create" button to start creating a new category
8. Enter a unique name in the title input field
9. Click the status dropdown and select "Inactive" status
10. Click the visibility dropdown and select "Internal" visibility
11. Click "Continue" to proceed to the next step
12. Click "Save" to create the category
13. Click "Categories" link to return to the categories list
14. Search for the created category using its title
15. Click the edit menu for the category
16. Click "Edit" to modify the category
17. Update the category title with a new unique name
18. Click "Save" to save the changes
19. Verify the category displays the updated title
20. Click the edit menu again
21. Click "Delete" to remove the category
22. Confirm the deletion by clicking "Delete"
23. Verify return to the Categories list page

## Assertions

- **url_match**: Categories page URL is correct after navigation
- **text_content**: Categories page title displays "Categories"
- **text_matched**: Continue button responds correctly during creation
- **text_matched**: Save button responds correctly during creation
- **text_matched**: Categories link responds correctly when returning to list
- **text_matched**: Edit button responds correctly when accessing edit mode
- **text_matched**: Save button responds correctly when updating category
- **text_content**: Updated category displays the new title correctly
- **text_matched**: Categories list page loads correctly after deletion
