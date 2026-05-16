#!/usr/bin/env python3
"""draft-orders.draft-orders-crud

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="draft-orders.draft-orders-crud",
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
region_select = Locator(
    name="region-select", tag="input",
    bbox=(959, 195, 346, 32),
    scroll_y=0,
    pos_type="abs",
)
europe_item = Locator(
    name="europe-item", tag="div",
    bbox=(963, 235, 338, 28),
    scroll_y=0,
    pos_type="abs",
)
sales_channel_select = Locator(
    name="sales-channel-select", tag="input",
    bbox=(959, 288, 346, 32),
    scroll_y=0,
    pos_type="abs",
)
default_sales_channel = Locator(
    name="default-sales-channel", tag="div",
    bbox=(963, 328, 338, 28),
    scroll_y=0,
    pos_type="abs",
)
email_input = Locator(
    name="email-input", tag="input",
    bbox=(959, 474, 346, 32),
    scroll_y=0,
    pos_type="abs",
)
country_select = Locator(
    name="country-select", tag="select",
    bbox=(959, 595, 346, 32),
    scroll_y=0,
    pos_type="abs",
)
first_name_input = Locator(
    name="first-name-input", tag="input",
    bbox=(959, 667, 165, 32),
    scroll_y=0,
    pos_type="abs",
)
last_name_input = Locator(
    name="last-name-input", tag="input",
    bbox=(1140, 667, 165, 32),
    scroll_y=0,
    pos_type="abs",
)
address_input = Locator(
    name="address-input", tag="input",
    bbox=(959, 811, 346, 32),
    scroll_y=0,
    pos_type="abs",
)
postal_code_input = Locator(
    name="postal-code-input", tag="input",
    bbox=(959, 955, 165, 32),
    scroll_y=0,
    pos_type="abs",
)
city_input = Locator(
    name="city-input", tag="input",
    bbox=(1140, 955, 165, 32),
    scroll_y=0,
    pos_type="abs",
)
save_button = Locator(
    name="save-button", tag="button",
    bbox=(1849, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
draft_order_detail_title = Locator(
    name="draft-order-detail-title", tag="h1",
    bbox=(306, 81, 122, 28),
    scroll_y=0,
    pos_type="abs",
    dynamic={'w': True},
)
draft_order_home = Locator(
    name="draft-order-home", tag="a",
    bbox=(266, 16, 77, 20),
    scroll_y=0,
    pos_type="abs",
)
search_text = Locator(
    name="search-text", tag="input",
    bbox=(1514, 81, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
order_item_1 = Locator(
    name="order-item-1", tag="td",
    bbox=(282, 219, 289, 48),
    scroll_y=0,
    pos_type="abs",
)
edit_menu = Locator(
    name="edit-menu", tag="button",
    bbox=(1350, 91, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
delete_draft_order = Locator(
    name="delete-draft-order", tag="div",
    bbox=(1258, 164, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
search_text_2 = Locator(
    name="search-text-2", tag="input",
    bbox=(1514, 81, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
no_results_found = Locator(
    name="no-results-found", tag="p",
    bbox=(1015, 269, 110, 22),
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
    await page.goto("/draft-orders")  # step 5
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/draft-orders*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 5: url_match /draft-orders — " + str(_e)) from _e
    await page.set_step(6)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1805, 95, "Create"]
    )
    assert _hit_el is not None, "step 6: text_matched — no element at bbox center"
    assert _hit_el == "Create", f"step 6: text_matched — expected \"Create\", got {_hit_el!r}"
    await page.click(create_1)  # step 6
    await page.wait(2000)
    await page.set_step(7)
    await page.click(region_select)  # step 7
    await page.wait(2000)
    await page.set_step(8)
    await page.click(europe_item)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    await page.click(sales_channel_select)  # step 9
    await page.wait(2000)
    await page.set_step(10)
    await page.click(default_sales_channel)  # step 10
    await page.wait(2000)
    await page.set_step(11)
    _run_email_input = ("test-" + secrets.token_hex(4) + "@example.com")
    await page.fill(email_input, _run_email_input)  # step 11
    await page.wait(2000)
    await page.set_step(12)
    await page.select_option(country_select, "us")  # step 12
    await page.wait(3000)
    await page.set_step(13)
    _run_first_name_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(first_name_input, _run_first_name_input)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    _run_last_name_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(last_name_input, _run_last_name_input)  # step 14
    await page.wait(2000)
    await page.set_step(15)
    await page.fill(address_input, "Test Street 1")  # step 15
    await page.wait(2000)
    await page.set_step(16)
    await page.fill(postal_code_input, "1234")  # step 16
    await page.wait(2000)
    await page.set_step(17)
    await page.fill(city_input, "Copenhagen")  # step 17
    await page.wait(2000)
    await page.set_step(18)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1872, 1041, "Save"]
    )
    assert _hit_el is not None, "step 18: text_matched — no element at bbox center"
    assert _hit_el == "Save", f"step 18: text_matched — expected \"Save\", got {_hit_el!r}"
    await page.click(save_button)  # step 18
    await page.wait(2000)
    await page.set_step(20)
    await page.click(draft_order_home)  # step 20
    await page.wait(2000)
    await page.set_step(21)
    await page.fill(search_text, _run_email_input)  # step 21
    await page.wait(2000)
    await page.set_step(22)
    await page.click(order_item_1)  # step 22
    await page.wait(2000)
    await page.set_step(23)
    await page.click(edit_menu)  # step 23
    await page.wait(2000)
    await page.set_step(24)
    await page.click(delete_draft_order)  # step 24
    await page.wait(2000)
    await page.set_step(25)
    await page.fill(search_text_2, _run_email_input)  # step 25
    await page.wait(2000)
    await page.set_step(26)
    await page.click(no_results_found)  # step 26
    await page.wait(2000)
    _expected = "No results found"
    _matched = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { if ((el.textContent || '').includes(exp)) return true; } return false; }",
        [1070, 280, _expected]
    )
    assert _matched, f"step 26: text_content — text at bbox does not contain {_expected!r}"


if __name__ == "__main__":
    scenario.run()
