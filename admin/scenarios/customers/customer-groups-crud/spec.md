---
name: customers.customer-groups-crud
url: /app/customer-groups
tags:
- empty-state
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
4. Click the "Continue with Email" button to log in
5. Navigate to the customer groups page
6. Click the "Create" button to start creating a new customer group
7. Enter a unique name in the name input field
8. Click the "Create" button to save the new customer group
9. Click the edit menu button for the created customer group
10. Click the "Edit" button to open the edit form
11. Enter a new unique name in the name input field
12. Click the "Save" button to update the customer group
13. Click the "Customer Groups" link to return to the main listing
14. Search for the updated customer group using the new name
15. Click on the customer group in the search results
16. Click the edit menu button for the customer group
17. Click the "Delete" button to initiate deletion
18. Click the "Delete" confirmation button to confirm deletion

## Assertions

- **url_match**: Verifies navigation to the customer groups page after login
- **element_visible**: Confirms the delete confirmation dialog appears
- **url_match**: Verifies return to the customer groups listing page after deletion

