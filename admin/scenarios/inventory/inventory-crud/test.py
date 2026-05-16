#!/usr/bin/env python3
"""inventory.inventory-crud

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
import random
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="inventory.inventory-crud",
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
    bbox=(1769, 91, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
title_input = Locator(
    name="title-input", tag="input",
    bbox=(601, 214, 351, 32),
    scroll_y=0,
    pos_type="abs",
)
sku_input = Locator(
    name="sku-input", tag="input",
    bbox=(968, 214, 351, 32),
    scroll_y=0,
    pos_type="abs",
)
next = Locator(
    name="next", tag="button",
    bbox=(1850, 1027, 45, 28),
    scroll_y=0,
    pos_type="abs",
)
in_stock_input = Locator(
    name="in-stock-input", tag="div",
    bbox=(159, 163, 149, 40),
    scroll_y=0,
    pos_type="abs",
)
save = Locator(
    name="save", tag="button",
    bbox=(1849, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
search_text = Locator(
    name="search-text", tag="input",
    bbox=(1609, 163, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
list_row_title = Locator(
    name="list-row-title", tag="div",
    bbox=(350, 256, 343, 47),
    scroll_y=0,
    pos_type="abs",
)
attributes_menu = Locator(
    name="attributes-menu", tag="button",
    bbox=(1806, 81, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
attributes_edit = Locator(
    name="attributes-edit", tag="a",
    bbox=(1696, 121, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
height_input = Locator(
    name="height-input", tag="input",
    bbox=(1377, 114, 510, 32),
    scroll_y=0,
    pos_type="abs",
)
attributes_save = Locator(
    name="attributes-save", tag="button",
    bbox=(1841, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
inventory_home = Locator(
    name="inventory-home", tag="a",
    bbox=(266, 16, 59, 20),
    scroll_y=0,
    pos_type="abs",
)
search_text_2 = Locator(
    name="search-text-2", tag="input",
    bbox=(1609, 163, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
row_menu = Locator(
    name="row-menu", tag="button",
    bbox=(1806, 266, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
row_delete = Locator(
    name="row-delete", tag="div",
    bbox=(1696, 348, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
delete_confirm = Locator(
    name="delete-confirm", tag="button",
    bbox=(1079, 572, 56, 28),
    scroll_y=0,
    pos_type="abs",
)
no_results = Locator(
    name="no-results", tag="div",
    bbox=(949, 372, 242, 72),
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
    await page.goto("/inventory")  # step 5
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/inventory*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 5: url_match /inventory — " + str(_e)) from _e
    await page.set_step(6)
    await page.click(create_1)  # step 6
    await page.wait(2000)
    await page.set_step(7)
    _run_title_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(title_input, _run_title_input)  # step 7
    await page.wait(2000)
    await page.set_step(8)
    _run_sku_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(sku_input, _run_sku_input)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    await page.click(next)  # step 9
    await page.wait(2000)
    await page.set_step(10)
    _run_in_stock_input = (str(random.randint(100, 999)))
    await page.fill(in_stock_input, _run_in_stock_input)  # step 10
    await page.wait(2000)
    await page.set_step(11)
    await page.click(save)  # step 11
    await page.wait(2000)
    await page.set_step(12)
    await page.fill(search_text, _run_title_input)  # step 12
    await page.wait(2000)
    await page.set_step(13)
    await page.click(list_row_title)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    await page.click(attributes_menu)  # step 14
    await page.wait(2000)
    await page.set_step(15)
    await page.click(attributes_edit)  # step 15
    await page.wait(2000)
    await page.set_step(16)
    _run_height_input = (str(random.randint(10, 99)))
    await page.fill(height_input, _run_height_input)  # step 16
    await page.wait(2000)
    await page.set_step(17)
    await page.click(attributes_save)  # step 17
    await page.wait(2000)
    await page.set_step(18)
    await page.click(inventory_home)  # step 18
    await page.wait(2000)
    await page.set_step(19)
    await page.fill(search_text_2, _run_title_input)  # step 19
    await page.wait(2000)
    await page.set_step(20)
    await page.click(row_menu)  # step 20
    await page.wait(2000)
    await page.set_step(21)
    await page.click(row_delete)  # step 21
    await page.wait(2000)
    await page.set_step(22)
    await page.click(delete_confirm)  # step 22
    await page.wait(2000)
    await page.set_step(23)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1070, 408, "No resultsTry changing the filters or search query"]
    )
    assert _hit_el is not None, "step 23: text_matched — no element at bbox center"
    assert _hit_el == "No resultsTry changing the filters or search query", f"step 23: text_matched — expected \"No resultsTry changing the filters or search query\", got {_hit_el!r}"
    await page.click(no_results)  # step 23
    await page.wait(2000)


if __name__ == "__main__":
    scenario.run()
