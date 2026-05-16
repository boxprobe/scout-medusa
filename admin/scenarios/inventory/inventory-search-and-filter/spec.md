---
name: inventory.inventory-search-and-filter
url: /login
tags:
- search
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
5. Navigate to the inventory page
6. Click the "Add filter" button and select SKU filter option
7. Select the "SKU" option from the filter dropdown
8. Enter "SWEATSHIRT-XL" in the SKU input field
9. Verify that the filter result displays the SKU "SWEATSHIRT-XL"
10. Click the clear filter button to reset the search
11. Enter "SHIRT-L-BLACK" in the search text field
12. Verify that the search result displays "SHIRT-L-BLACK"

## Assertions

- **url_match**: Verify successful navigation to the inventory page (/inventory)
- **text_content**: Verify that SKU filter returns correct product "SWEATSHIRT-XL"
- **text_content**: Verify that text search returns correct product "SHIRT-L-BLACK"
