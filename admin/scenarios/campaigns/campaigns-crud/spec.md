---
name: campaigns.campaigns-crud
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
4. Click "Continue with Email" button to log in
5. Navigate to the campaigns page
6. Verify the campaigns page displays with "Campaigns" title
7. Click the "Create" button to start creating a new campaign
8. Enter a unique name in the name-input field
9. Enter the same unique name in the identifier-input field
10. Enter the same unique name in the description-input field
11. Select the usage limit option by clicking the usage-radio button
12. Set the usage limit to 100 in the limit-input field
13. Click the "Create" button to save the new campaign
14. Verify the campaign details page shows the created campaign
15. Click the edit-menu button to open campaign options
16. Click the "Edit" button to enter edit mode
17. Enter a new unique name in the new-name-input field
18. Click "Save" button to save the changes
19. Verify the updated campaign name is displayed
20. Click the edit-menu button again to open campaign options
21. Click the "Delete" button to initiate deletion
22. Click the "Delete" confirmation button to confirm deletion
23. Verify the campaigns list shows "No records"

## Assertions

- **url_match**: Campaigns page URL is correctly accessed
- **text_matched**: Create button functionality is confirmed
- **text_content**: Created campaign name matches the input value
- **text_content**: Updated campaign name matches the new input value  
- **text_matched**: Campaign deletion is confirmed by "No records" message
