#!/usr/bin/env python3
"""customers.customers-crud

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="customers.customers-crud",
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
    name="create-1", tag="button",
    bbox=(1776, 81, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
first_name = Locator(
    name="first-name", tag="input",
    bbox=(600, 227, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
last_name = Locator(
    name="last-name", tag="input",
    bbox=(968, 227, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
email_input = Locator(
    name="email-input", tag="input",
    bbox=(600, 303, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
create_2 = Locator(
    name="create-2", tag="button",
    bbox=(1837, 1027, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
customers_home = Locator(
    name="customers-home", tag="a",
    bbox=(266, 16, 68, 20),
    scroll_y=0,
    pos_type="abs",
)
search_text = Locator(
    name="search-text", tag="input",
    bbox=(1609, 142, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
list_email = Locator(
    name="list-email", tag="div",
    bbox=(299, 236, 338, 47),
    scroll_y=0,
    pos_type="abs",
)
edit_menu_2 = Locator(
    name="edit-menu-2", tag="button",
    bbox=(1350, 81, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_2 = Locator(
    name="edit-2", tag="a",
    bbox=(1258, 121, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
company_input = Locator(
    name="company-input", tag="input",
    bbox=(1377, 342, 510, 32),
    scroll_y=0,
    pos_type="abs",
)
save_2 = Locator(
    name="save-2", tag="button",
    bbox=(1841, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_menu_3 = Locator(
    name="edit-menu-3", tag="button",
    bbox=(1350, 81, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
delete_button = Locator(
    name="delete-button", tag="div",
    bbox=(1258, 163, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
delete_modal = Locator(
    name="delete-modal", tag="form",
    bbox=(761, 365, 398, 350),
    scroll_y=0,
    pos_type="abs",
    dynamic={'h': True},
)
delete_confirm_input = Locator(
    name="delete-confirm-input", tag="input",
    bbox=(785, 582, 350, 32),
    scroll_y=0,
    pos_type="rel",
    parent="delete-modal",
    pos_offset={'left': 24, 'bottom': 96},
)
delete_confirm_button = Locator(
    name="delete-confirm-button", tag="button",
    bbox=(1079, 663, 56, 28),
    scroll_y=0,
    pos_type="rel",
    parent="delete-modal",
    pos_offset={'right': 24, 'bottom': 24},
)
customers_title = Locator(
    name="customers-title", tag="h1",
    bbox=(299, 81, 94, 28),
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
    await page.goto("/customers")  # step 5
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/customers*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 5: url_match /customers — " + str(_e)) from _e
    await page.set_step(6)
    await page.click(create_1)  # step 6
    await page.wait(2000)
    await page.set_step(7)
    _run_first_name = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(first_name, _run_first_name)  # step 7
    await page.wait(2000)
    await page.set_step(8)
    _run_last_name = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(last_name, _run_last_name)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    _run_email_input = ("test-" + secrets.token_hex(4) + "@example.com")
    await page.fill(email_input, _run_email_input)  # step 9
    await page.wait(2000)
    await page.set_step(10)
    await page.click(create_2)  # step 10
    await page.wait(2000)
    await page.set_step(11)
    await page.click(customers_home)  # step 11
    await page.wait(2000)
    await page.set_step(12)
    await page.fill(search_text, _run_email_input)  # step 12
    await page.wait(2000)
    await page.set_step(13)
    await page.click(list_email)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    await page.click(edit_menu_2)  # step 14
    await page.wait(2000)
    await page.set_step(15)
    await page.click(edit_2)  # step 15
    await page.wait(2000)
    await page.set_step(16)
    _run_company_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(company_input, _run_company_input)  # step 16
    await page.wait(2000)
    await page.set_step(17)
    await page.click(save_2)  # step 17
    await page.wait(2000)
    await page.set_step(18)
    await page.click(edit_menu_3)  # step 18
    await page.wait(2000)
    await page.set_step(19)
    await page.click(delete_button)  # step 19
    await page.wait(2000)
    await page.set_step(21)
    await page.fill(delete_confirm_input, _run_email_input)  # step 21
    await page.wait(2000)
    await page.set_step(22)
    await page.click(delete_confirm_button)  # step 22
    await page.wait(2000)


if __name__ == "__main__":
    scenario.run()
