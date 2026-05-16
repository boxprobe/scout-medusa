---
name: draft-orders.draft-orders-crud
url: /login
tags:
- core
- crud
priority: critical
---

## Preconditions

- logged_in: False
- page: /login

## Steps

1. Navigate to login page
2. Enter admin credentials in email field
3. Enter admin credentials in password field
4. Click "Continue with Email" button to log in
5. Navigate to draft orders page
6. Click "Create" button to start creating a new draft order
7. Click region select dropdown
8. Select "Europe" from region options
9. Click sales channel select dropdown
10. Select "Default Sales Channel" from available options
11. Enter a unique email address in the email input field
12. Select "us" from the country dropdown
13. Enter a unique name in the first name field
14. Enter a unique name in the last name field
15. Enter "Test Street 1" in the address field
16. Enter "1234" in the postal code field
17. Enter "Copenhagen" in the city field
18. Click "Save" button to create the draft order
19. Verify draft order detail page loads with order title
20. Click "Draft Orders" link to return to the list
21. Search for the created order using the email address
22. Click on the found order item to view details
23. Click the edit menu button
24. Click "Delete draft order" option
25. Search again for the deleted order using the same email
26. Verify no results are found

## Assertions

- **url_match**: Draft orders page URL matches expected pattern
- **text_matched**: "Create" button text is correctly displayed
- **text_matched**: "Save" button text is correctly displayed
- **text_content**: Draft order detail page displays order title containing "Draft Order #"
- **text_content**: Search results show "No results found" after deletion, confirming order was successfully deleted

