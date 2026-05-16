#!/usr/bin/env python3
"""collections.collections-crud

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="collections.collections-crud",
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
    bbox=(1776, 91, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
title_input = Locator(
    name="title-input", tag="input",
    bbox=(600, 227, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
handle_input = Locator(
    name="handle-input", tag="input",
    bbox=(968, 227, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
create_2 = Locator(
    name="create-2", tag="button",
    bbox=(1837, 1027, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
list_collection_title = Locator(
    name="list-collection-title", tag="h1",
    bbox=(306, 81, 18, 28),
    scroll_y=0,
    pos_type="abs",
    dynamic={'w': True},
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
new_title_input = Locator(
    name="new-title-input", tag="input",
    bbox=(1377, 114, 510, 32),
    scroll_y=0,
    pos_type="abs",
)
save_button = Locator(
    name="save-button", tag="button",
    bbox=(1841, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
updated_collection_title = Locator(
    name="updated-collection-title", tag="h1",
    bbox=(306, 81, 18, 28),
    scroll_y=0,
    pos_type="abs",
    dynamic={'w': True},
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
    bbox=(1069, 572, 66, 28),
    scroll_y=0,
    pos_type="abs",
)
no_records_text_2 = Locator(
    name="no-records-text-2", tag="h1",
    bbox=(306, 81, 213, 28),
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
    await page.goto("/collections")  # step 5
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/collections*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 5: url_match /collections — " + str(_e)) from _e
    await page.set_step(6)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1805, 105, "Create"]
    )
    assert _hit_el is not None, "step 6: text_matched — no element at bbox center"
    assert _hit_el == "Create", f"step 6: text_matched — expected \"Create\", got {_hit_el!r}"
    await page.click(create_1)  # step 6
    await page.wait(2000)
    await page.set_step(7)
    _run_title_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(title_input, _run_title_input)  # step 7
    await page.wait(2000)
    await page.set_step(8)
    _run_handle_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(handle_input, _run_handle_input)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1866, 1041, "Create"]
    )
    assert _hit_el is not None, "step 9: text_matched — no element at bbox center"
    assert _hit_el == "Create", f"step 9: text_matched — expected \"Create\", got {_hit_el!r}"
    await page.click(create_2)  # step 9
    await page.wait(2000)
    await page.set_step(11)
    await page.click(edit_menu)  # step 11
    await page.wait(2000)
    await page.set_step(12)
    await page.click(edit_button)  # step 12
    await page.wait(2000)
    await page.set_step(13)
    _run_new_title_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(new_title_input, _run_new_title_input)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    await page.click(save_button)  # step 14
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


if __name__ == "__main__":
    scenario.run()
