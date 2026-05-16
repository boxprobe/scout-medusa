#!/usr/bin/env python3
"""locations.location-edit

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
import random
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="locations.location-edit",
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
    bbox=(1320, 91, 58, 28),
    scroll_y=0,
    pos_type="abs",
)
name_input = Locator(
    name="name-input", tag="input",
    bbox=(608, 227, 344, 28),
    scroll_y=0,
    pos_type="abs",
)
address_input = Locator(
    name="address-input", tag="input",
    bbox=(608, 315, 344, 28),
    scroll_y=0,
    pos_type="abs",
)
country_list = Locator(
    name="country-list", tag="button",
    bbox=(608, 459, 344, 32),
    scroll_y=0,
    pos_type="abs",
)
albania = Locator(
    name="albania", tag="span",
    bbox=(643, 545, 297, 20),
    scroll_y=0,
    pos_type="abs",
)
save_1 = Locator(
    name="save-1", tag="button",
    bbox=(1849, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_menu = Locator(
    name="edit-menu", tag="button",
    bbox=(1350, 92, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_button = Locator(
    name="edit-button", tag="a",
    bbox=(1258, 132, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
post_code_input = Locator(
    name="post-code-input", tag="input",
    bbox=(1377, 330, 510, 28),
    scroll_y=0,
    pos_type="abs",
)
save_2 = Locator(
    name="save-2", tag="button",
    bbox=(1841, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
locations_home = Locator(
    name="locations-home", tag="a",
    bbox=(349, 16, 61, 20),
    scroll_y=0,
    pos_type="abs",
)
search_text = Locator(
    name="search-text", tag="input",
    bbox=(1130, 91, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
edit_menu_2 = Locator(
    name="edit-menu-2", tag="button",
    bbox=(1350, 205, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
delete_button = Locator(
    name="delete-button", tag="div",
    bbox=(1258, 287, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
delete_confirm = Locator(
    name="delete-confirm", tag="button",
    bbox=(1069, 572, 66, 28),
    scroll_y=0,
    pos_type="abs",
)
no_records = Locator(
    name="no-records", tag="p",
    bbox=(805, 244, 74, 22),
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
    await page.goto("/settings/locations")  # step 5
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/settings/locations*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 5: url_match /settings/locations — " + str(_e)) from _e
    await page.set_step(6)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1349, 105, "Create"]
    )
    assert _hit_el is not None, "step 6: text_matched — no element at bbox center"
    assert _hit_el == "Create", f"step 6: text_matched — expected \"Create\", got {_hit_el!r}"
    await page.click(create_1)  # step 6
    await page.wait(2000)
    await page.set_step(7)
    _run_name_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(name_input, _run_name_input)  # step 7
    await page.wait(2000)
    await page.set_step(8)
    _run_address_input = ("test-" + secrets.token_hex(4)[:6])
    await page.fill(address_input, _run_address_input)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    await page.click(country_list)  # step 9
    await page.wait(2000)
    await page.set_step(10)
    await page.click(albania)  # step 10
    await page.wait(2000)
    await page.set_step(11)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1872, 1041, "Save"]
    )
    assert _hit_el is not None, "step 11: text_matched — no element at bbox center"
    assert _hit_el == "Save", f"step 11: text_matched — expected \"Save\", got {_hit_el!r}"
    await page.click(save_1)  # step 11
    await page.wait(2000)
    await page.set_step(12)
    await page.click(edit_menu)  # step 12
    await page.wait(2000)
    await page.set_step(13)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1364, 148, "Edit"]
    )
    assert _hit_el is not None, "step 13: text_matched — no element at bbox center"
    assert _hit_el == "Edit", f"step 13: text_matched — expected \"Edit\", got {_hit_el!r}"
    await page.click(edit_button)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    _run_post_code_input = (str(random.randint(100000, 999999)))
    await page.fill(post_code_input, _run_post_code_input)  # step 14
    await page.wait(2000)
    await page.set_step(15)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1864, 1041, "Save"]
    )
    assert _hit_el is not None, "step 15: text_matched — no element at bbox center"
    assert _hit_el == "Save", f"step 15: text_matched — expected \"Save\", got {_hit_el!r}"
    await page.click(save_2)  # step 15
    await page.wait(2000)
    await page.set_step(16)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [379, 26, "Locations"]
    )
    assert _hit_el is not None, "step 16: text_matched — no element at bbox center"
    assert _hit_el == "Locations", f"step 16: text_matched — expected \"Locations\", got {_hit_el!r}"
    await page.click(locations_home)  # step 16
    await page.wait(2000)
    await page.set_step(17)
    await page.fill(search_text, _run_name_input)  # step 17
    await page.wait(2000)
    await page.set_step(18)
    await page.click(edit_menu_2)  # step 18
    await page.wait(2000)
    await page.set_step(19)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1364, 303, "Delete"]
    )
    assert _hit_el is not None, "step 19: text_matched — no element at bbox center"
    assert _hit_el == "Delete", f"step 19: text_matched — expected \"Delete\", got {_hit_el!r}"
    await page.click(delete_button)  # step 19
    await page.wait(2000)
    await page.set_step(20)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1102, 586, "Remove"]
    )
    assert _hit_el is not None, "step 20: text_matched — no element at bbox center"
    assert _hit_el == "Remove", f"step 20: text_matched — expected \"Remove\", got {_hit_el!r}"
    await page.click(delete_confirm)  # step 20
    await page.wait(2000)
    await page.set_step(21)
    await page.click(no_records)  # step 21
    await page.wait(2000)
    _expected = "No records"
    _matched = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { if ((el.textContent || '').includes(exp)) return true; } return false; }",
        [842, 255, _expected]
    )
    assert _matched, f"step 21: text_content — text at bbox does not contain {_expected!r}"


if __name__ == "__main__":
    scenario.run()
