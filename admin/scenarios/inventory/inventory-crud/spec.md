---
name: inventory.inventory-crud
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
4. Click the "Continue with Email" button to log in
5. Navigate to the inventory page and verify the URL matches /inventory
6. Click the "Create" link to start creating a new inventory item
7. Enter a unique name in the title-input field
8. Enter a unique name in the sku-input field
9. Click the "Next" button to proceed to the next step
10. Enter a random 3-digit number in the in-stock-input field
11. Click the "Save" button to create the inventory item
12. Search for the created item using the search-text field with the title value
13. Click on the list-row-title to select the found inventory item
14. Click the attributes-menu button to open the attributes menu
15. Click the "Edit" link in the attributes menu to edit item attributes
16. Enter a random 2-digit number in the height-input field
17. Click the "Save" button to save the attribute changes
18. Click the "Inventory" link to return to the inventory home page
19. Search again for the created item using search-text-2 field
20. Click the row-menu button for the found item
21. Click the "Delete" option from the row menu
22. Click the "Delete" button to confirm deletion
23. Verify that the item is deleted by confirming "No results" message appears

## Assertions

- **url_match**: Inventory page URL matches /inventory pattern after navigation
- **text_content**: "No results" message is displayed after item deletion, confirming successful removal

