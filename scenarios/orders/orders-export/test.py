#!/usr/bin/env python3
"""orders.orders-export

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
import random
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="orders.orders-export",
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
europe_option = Locator(
    name="europe-option", tag="div",
    bbox=(963, 235, 338, 28),
    scroll_y=0,
    pos_type="abs",
)
channel_select = Locator(
    name="channel-select", tag="input",
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
post_code_input = Locator(
    name="post-code-input", tag="input",
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
convert_to_order = Locator(
    name="convert-to-order", tag="button",
    bbox=(1259, 373, 119, 28),
    scroll_y=0,
    pos_type="abs",
)
convert_to_order_confirm = Locator(
    name="convert-to-order-confirm", tag="button",
    bbox=(1069, 572, 66, 28),
    scroll_y=0,
    pos_type="abs",
)
orders_home = Locator(
    name="orders-home", tag="a",
    bbox=(266, 16, 42, 20),
    scroll_y=0,
    pos_type="abs",
)
export_1 = Locator(
    name="export-1", tag="a",
    bbox=(1777, 81, 57, 28),
    scroll_y=0,
    pos_type="abs",
)
export_2 = Locator(
    name="export-2", tag="button",
    bbox=(1830, 1027, 57, 28),
    scroll_y=0,
    pos_type="abs",
)
orders_title = Locator(
    name="orders-title", tag="h1",
    bbox=(306, 81, 59, 28),
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
    await page.click(europe_option)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    await page.click(channel_select)  # step 9
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
    await page.wait(2000)
    await page.set_step(13)
    _run_first_name_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(first_name_input, _run_first_name_input)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    _run_last_name_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(last_name_input, _run_last_name_input)  # step 14
    await page.wait(2000)
    await page.set_step(15)
    _run_address_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(address_input, _run_address_input)  # step 15
    await page.wait(2000)
    await page.set_step(16)
    _run_post_code_input = (str(random.randint(1000, 9999)))
    await page.fill(post_code_input, _run_post_code_input)  # step 16
    await page.wait(2000)
    await page.set_step(17)
    await page.fill(city_input, "tokoy")  # step 17
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
    await page.set_step(19)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1318, 387, "Convert to order"]
    )
    assert _hit_el is not None, "step 19: text_matched — no element at bbox center"
    assert _hit_el == "Convert to order", f"step 19: text_matched — expected \"Convert to order\", got {_hit_el!r}"
    await page.click(convert_to_order)  # step 19
    await page.wait(2000)
    await page.set_step(20)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1102, 586, "Confirm"]
    )
    assert _hit_el is not None, "step 20: text_matched — no element at bbox center"
    assert _hit_el == "Confirm", f"step 20: text_matched — expected \"Confirm\", got {_hit_el!r}"
    await page.click(convert_to_order_confirm)  # step 20
    await page.wait(2000)
    await page.set_step(21)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [287, 26, "Orders"]
    )
    assert _hit_el is not None, "step 21: text_matched — no element at bbox center"
    assert _hit_el == "Orders", f"step 21: text_matched — expected \"Orders\", got {_hit_el!r}"
    await page.click(orders_home)  # step 21
    await page.wait(2000)
    await page.set_step(22)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1805, 95, "Export"]
    )
    assert _hit_el is not None, "step 22: text_matched — no element at bbox center"
    assert _hit_el == "Export", f"step 22: text_matched — expected \"Export\", got {_hit_el!r}"
    await page.click(export_1)  # step 22
    await page.wait(2000)
    await page.set_step(23)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1858, 1041, "Export"]
    )
    assert _hit_el is not None, "step 23: text_matched — no element at bbox center"
    assert _hit_el == "Export", f"step 23: text_matched — expected \"Export\", got {_hit_el!r}"
    await page.click(export_2)  # step 23
    await page.wait(2000)
    await page.set_step(24)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [335, 95, "Orders"]
    )
    assert _hit_el is not None, "step 24: text_matched — no element at bbox center"
    assert _hit_el == "Orders", f"step 24: text_matched — expected \"Orders\", got {_hit_el!r}"
    await page.click(orders_title)  # step 24
    await page.wait(2000)


if __name__ == "__main__":
    scenario.run()
