---
name: customers.customers-crud
url: /app/customers
tags:
- core
- crud
priority: critical
---

## Preconditions

- logged_in: False
- page: /login

## Steps

1. Navigate to the login page
2. Enter admin credentials in the email field
3. Enter admin credentials in the password field
4. Click the "Continue with Email" button to log in
5. Navigate to the customers page
6. Click the "Create" button to start creating a new customer
7. Enter a unique name in the first-name field
8. Enter a unique name in the last-name field
9. Enter a unique email in the email-input field
10. Click the "Create" button to save the new customer
11. Click the "Customers" link to return to the customers list
12. Search for the created customer using their email address
13. Click on the customer's email in the search results
14. Click the edit-menu button for the customer
15. Click the "Edit" option from the menu
16. Update the company-input field with a unique name
17. Click the "Save" button to save the changes
18. Click the edit-menu button again
19. Click the "Delete" option from the menu
20. Verify the delete confirmation modal appears
21. Enter the customer's email in the delete-confirm-input field
22. Click the "Delete" button to confirm deletion
23. Return to the customers page

## Assertions

- **url_match**: Verify navigation to /customers page is successful
- **text_content**: Verify the "Customers" page title is displayed after deletion
