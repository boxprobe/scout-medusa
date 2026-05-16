---
name: orders.orders-export
url: /login
tags:
- core
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
5. Navigate to the draft orders page
6. Click "Create" button to start creating a new draft order
7. Click the region select dropdown
8. Select "Europe" from the region options
9. Click the channel select dropdown
10. Select "Default Sales Channel" from the channel options
11. Enter a unique email address in the email input field
12. Select "US" from the country dropdown
13. Enter a unique name in the first name field
14. Enter a unique name in the last name field
15. Enter a unique address in the address field
16. Enter a 4-digit number in the post code field
17. Enter "tokoy" in the city field
18. Click "Save" button to save the draft order
19. Click "Convert to order" button to convert the draft to an order
20. Click "Confirm" button to confirm the order conversion
21. Click "Orders" link to navigate to the orders overview
22. Click "Export" link to access the export functionality
23. Click "Export" button to initiate the orders export
24. Click "Orders" title to return to the orders page

## Assertions

- **url_match**: Verify navigation to draft orders page is successful
- **text_matched**: Verify "Create" button is clickable and responsive
- **text_matched**: Verify "Save" button successfully saves the draft order
- **text_matched**: Verify "Convert to order" button is available and functional
- **text_matched**: Verify order conversion confirmation works properly
- **text_matched**: Verify "Orders" navigation link is accessible
- **text_matched**: Verify "Export" functionality is available in orders section
- **text_matched**: Verify export process can be initiated successfully
- **text_matched**: Verify return to orders page after export completion
