#!/usr/bin/env python3
"""categories.categories-crud

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="categories.categories-crud",
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
categories_title = Locator(
    name="categories-title", tag="h1",
    bbox=(306, 81, 541, 28),
    scroll_y=0,
    pos_type="abs",
)
create_1 = Locator(
    name="create-1", tag="a",
    bbox=(1776, 91, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
title_input = Locator(
    name="title-input", tag="input",
    bbox=(600, 235, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
status_dropdown = Locator(
    name="status-dropdown", tag="button",
    bbox=(600, 447, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
select_inactive = Locator(
    name="select-inactive", tag="div",
    bbox=(604, 527, 344, 32),
    scroll_y=0,
    pos_type="abs",
)
visibility_dropdown = Locator(
    name="visibility-dropdown", tag="button",
    bbox=(968, 447, 352, 32),
    scroll_y=0,
    pos_type="abs",
)
select_internal = Locator(
    name="select-internal", tag="div",
    bbox=(972, 527, 344, 32),
    scroll_y=0,
    pos_type="abs",
)
continue_button = Locator(
    name="continue-button", tag="button",
    bbox=(1823, 1027, 72, 28),
    scroll_y=0,
    pos_type="abs",
)
save_button = Locator(
    name="save-button", tag="button",
    bbox=(1849, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
category_home = Locator(
    name="category-home", tag="a",
    bbox=(266, 16, 68, 20),
    scroll_y=0,
    pos_type="abs",
    dynamic={'w': True},
)
search_text = Locator(
    name="search-text", tag="input",
    bbox=(1652, 163, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_menu = Locator(
    name="edit-menu", tag="button",
    bbox=(1806, 266, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_button = Locator(
    name="edit-button", tag="a",
    bbox=(1696, 306, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
new_title_input = Locator(
    name="new-title-input", tag="input",
    bbox=(1377, 114, 510, 32),
    scroll_y=0,
    pos_type="abs",
)
save_button_2 = Locator(
    name="save-button-2", tag="button",
    bbox=(1841, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
updated_category_item = Locator(
    name="updated-category-item", tag="h1",
    bbox=(306, 81, 102, 28),
    scroll_y=0,
    pos_type="abs",
    dynamic={'w': True},
)
edit_menu_2 = Locator(
    name="edit-menu-2", tag="button",
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
delete_confirm_button = Locator(
    name="delete-confirm-button", tag="button",
    bbox=(1079, 572, 56, 28),
    scroll_y=0,
    pos_type="abs",
)
categories_list_title = Locator(
    name="categories-list-title", tag="h1",
    bbox=(306, 81, 541, 28),
    scroll_y=0,
    pos_type="abs",
    dynamic={'w': True},
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
    await page.goto("/categories")  # step 5
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/categories*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 5: url_match /categories — " + str(_e)) from _e
    await page.set_step(7)
    await page.click(create_1)  # step 7
    await page.wait(2000)
    await page.set_step(8)
    _run_title_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(title_input, _run_title_input)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    await page.click(status_dropdown)  # step 9
    await page.wait(2000)
    await page.set_step(10)
    await page.click(select_inactive)  # step 10
    await page.wait(2000)
    await page.set_step(11)
    await page.click(visibility_dropdown)  # step 11
    await page.wait(2000)
    await page.set_step(12)
    await page.click(select_internal)  # step 12
    await page.wait(2000)
    await page.set_step(13)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1859, 1041, "Continue"]
    )
    assert _hit_el is not None, "step 13: text_matched — no element at bbox center"
    assert _hit_el == "Continue", f"step 13: text_matched — expected \"Continue\", got {_hit_el!r}"
    await page.click(continue_button)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1872, 1041, "Save"]
    )
    assert _hit_el is not None, "step 14: text_matched — no element at bbox center"
    assert _hit_el == "Save", f"step 14: text_matched — expected \"Save\", got {_hit_el!r}"
    await page.click(save_button)  # step 14
    await page.wait(2000)
    await page.set_step(15)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [300, 26, "Categories"]
    )
    assert _hit_el is not None, "step 15: text_matched — no element at bbox center"
    assert _hit_el == "Categories", f"step 15: text_matched — expected \"Categories\", got {_hit_el!r}"
    await page.click(category_home)  # step 15
    await page.wait(2000)
    await page.set_step(16)
    await page.fill(search_text, _run_title_input)  # step 16
    await page.wait(2000)
    await page.set_step(17)
    await page.click(edit_menu)  # step 17
    await page.wait(2000)
    await page.set_step(18)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1802, 322, "Edit"]
    )
    assert _hit_el is not None, "step 18: text_matched — no element at bbox center"
    assert _hit_el == "Edit", f"step 18: text_matched — expected \"Edit\", got {_hit_el!r}"
    await page.click(edit_button)  # step 18
    await page.wait(2000)
    await page.set_step(19)
    _run_new_title_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(new_title_input, _run_new_title_input)  # step 19
    await page.wait(2000)
    await page.set_step(20)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1864, 1041, "Save"]
    )
    assert _hit_el is not None, "step 20: text_matched — no element at bbox center"
    assert _hit_el == "Save", f"step 20: text_matched — expected \"Save\", got {_hit_el!r}"
    await page.click(save_button_2)  # step 20
    await page.wait(2000)
    await page.set_step(22)
    await page.click(edit_menu_2)  # step 22
    await page.wait(2000)
    await page.set_step(23)
    await page.click(delete_button)  # step 23
    await page.wait(2000)
    await page.set_step(24)
    await page.click(delete_confirm_button)  # step 24
    await page.wait(2000)


if __name__ == "__main__":
    scenario.run()
