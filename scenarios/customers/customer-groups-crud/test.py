#!/usr/bin/env python3
"""customers.customer-groups-crud

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="customers.customer-groups-crud",
    base_url="http://localhost:19000/app",
    viewport_width=1920,
    viewport_height=1080,
    wait_ms=2000,
)

# ── Locators ────────────────────────────────────
email = Locator(
    name="email", tag="input",
    bbox=(820, 505, 280, 32),
    scroll_y=0,
    pos_type="abs",
)
password = Locator(
    name="password", tag="input",
    bbox=(820, 549, 280, 32),
    scroll_y=0,
    pos_type="abs",
)
continue_with_email = Locator(
    name="continue-with-email", tag="button",
    bbox=(820, 605, 280, 32),
    scroll_y=0,
    pos_type="abs",
)
create_1 = Locator(
    name="create-1", tag="a",
    bbox=(1776, 81, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
name_input = Locator(
    name="name-input", tag="input",
    bbox=(600, 235, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
create_2 = Locator(
    name="create-2", tag="button",
    bbox=(1837, 1027, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_menu = Locator(
    name="edit-menu", tag="button",
    bbox=(1806, 81, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_button = Locator(
    name="edit-button", tag="a",
    bbox=(1696, 121, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
new_name_input = Locator(
    name="new-name-input", tag="input",
    bbox=(1377, 114, 510, 28),
    scroll_y=0,
    pos_type="abs",
)
save_button = Locator(
    name="save-button", tag="button",
    bbox=(1841, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
customer_groups_home = Locator(
    name="customer-groups-home", tag="a",
    bbox=(266, 16, 109, 20),
    scroll_y=0,
    pos_type="abs",
)
search_text = Locator(
    name="search-text", tag="input",
    bbox=(1586, 81, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
list_group_name = Locator(
    name="list-group-name", tag="td",
    bbox=(282, 219, 362, 48),
    scroll_y=0,
    pos_type="abs",
)
edit_menu_2 = Locator(
    name="edit-menu-2", tag="button",
    bbox=(1806, 81, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
delete_button = Locator(
    name="delete-button", tag="div",
    bbox=(1696, 163, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
delete_confirm_button = Locator(
    name="delete-confirm-button", tag="button",
    bbox=(1079, 572, 56, 28),
    scroll_y=0,
    pos_type="abs",
)

@scenario.test
async def test(page: Page):
    await page.set_step(1)
    await page.goto("/login")  # step 1
    await page.wait(2000)
    await page.set_step(2)
    await page.fill(email, "admin@medusa-test.com")  # step 2
    await page.wait(2000)
    await page.set_step(3)
    await page.fill(password, "supersecret")  # step 3
    await page.wait(2000)
    await page.set_step(4)
    await page.click(continue_with_email)  # step 4
    await page.wait(2000)
    await page.set_step(5)
    await page.goto("/customer-groups")  # step 5
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/customer-groups*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 5: url_match /customer-groups — " + str(_e)) from _e
    await page.set_step(6)
    await page.click(create_1)  # step 6
    await page.wait(2000)
    await page.set_step(7)
    _run_name_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(name_input, _run_name_input)  # step 7
    await page.wait(2000)
    await page.set_step(8)
    await page.click(create_2)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    await page.click(edit_menu)  # step 9
    await page.wait(2000)
    await page.set_step(10)
    await page.click(edit_button)  # step 10
    await page.wait(2000)
    await page.set_step(11)
    _run_new_name_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(new_name_input, _run_new_name_input)  # step 11
    await page.wait(2000)
    await page.set_step(12)
    await page.click(save_button)  # step 12
    await page.wait(2000)
    await page.set_step(13)
    await page.click(customer_groups_home)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    await page.fill(search_text, _run_new_name_input)  # step 14
    await page.wait(2000)
    await page.set_step(15)
    await page.click(list_group_name)  # step 15
    await page.wait(2000)
    await page.set_step(16)
    await page.click(edit_menu_2)  # step 16
    await page.wait(2000)
    await page.set_step(17)
    await page.click(delete_button)  # step 17
    await page.wait(2000)
    await page.set_step(18)
    await page.click(delete_confirm_button)  # step 18
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/customer-groups*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 18: url_match /customer-groups — " + str(_e)) from _e


if __name__ == "__main__":
    scenario.run()
