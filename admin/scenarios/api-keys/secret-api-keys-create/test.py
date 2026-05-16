#!/usr/bin/env python3
"""api-keys.secret-api-keys-create

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
import secrets
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="api-keys.secret-api-keys-create",
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
    bbox=(608, 227, 344, 32),
    scroll_y=0,
    pos_type="abs",
)
save_button = Locator(
    name="save-button", tag="button",
    bbox=(1849, 1027, 46, 28),
    scroll_y=0,
    pos_type="abs",
)
token_dialog_continue = Locator(
    name="token-dialog-continue", tag="button",
    bbox=(1263, 615, 72, 28),
    scroll_y=0,
    pos_type="abs",
)
list_key_title = Locator(
    name="list-key-title", tag="h1",
    bbox=(306, 81, 54, 28),
    scroll_y=0,
    pos_type="abs",
    dynamic={'w': True},
)
delete_menu = Locator(
    name="delete-menu", tag="button",
    bbox=(1806, 81, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
revoke_button = Locator(
    name="revoke-button", tag="div",
    bbox=(1696, 163, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
remove_api_key_button = Locator(
    name="remove-api-key-button", tag="button",
    bbox=(1024, 572, 111, 28),
    scroll_y=0,
    pos_type="abs",
)
revoked = Locator(
    name="revoked", tag="span",
    bbox=(1715, 85, 75, 20),
    scroll_y=0,
    pos_type="abs",
)
edit_menu_2 = Locator(
    name="edit-menu-2", tag="button",
    bbox=(1806, 81, 28, 28),
    scroll_y=0,
    pos_type="abs",
)
delete_api_key_2 = Locator(
    name="delete-api-key-2", tag="div",
    bbox=(1696, 163, 212, 32),
    scroll_y=0,
    pos_type="abs",
)
delete_api_key_confirm = Locator(
    name="delete-api-key-confirm", tag="button",
    bbox=(1079, 572, 56, 28),
    scroll_y=0,
    pos_type="abs",
)
secret_api_keys = Locator(
    name="secret-api-keys", tag="h1",
    bbox=(306, 81, 451, 28),
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
    await page.goto("/settings/secret-api-keys")  # step 5
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/settings/secret-api-keys*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 5: url_match /settings/secret-api-keys — " + str(_e)) from _e
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
    await page.click(save_button)  # step 8
    await page.wait(2000)
    await page.set_step(9)
    await page.click(token_dialog_continue)  # step 9
    await page.wait(2000)
    await page.set_step(10)
    await page.click(list_key_title)  # step 10
    await page.wait(2000)
    _expected = _run_title_input
    _matched = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { if ((el.textContent || '').includes(exp)) return true; } return false; }",
        [333, 95, _expected]
    )
    assert _matched, f"step 10: text_content — text at bbox does not contain {_expected!r}"
    await page.set_step(11)
    await page.click(delete_menu)  # step 11
    await page.wait(2000)
    await page.set_step(12)
    await page.click(revoke_button)  # step 12
    await page.wait(2000)
    await page.set_step(13)
    await page.click(remove_api_key_button)  # step 13
    await page.wait(2000)
    await page.set_step(14)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [1752, 95, "Revoked"]
    )
    assert _hit_el is not None, "step 14: text_matched — no element at bbox center"
    assert _hit_el == "Revoked", f"step 14: text_matched — expected \"Revoked\", got {_hit_el!r}"
    await page.click(revoked)  # step 14
    await page.wait(2000)
    await page.set_step(15)
    await page.click(edit_menu_2)  # step 15
    await page.wait(2000)
    await page.set_step(16)
    await page.click(delete_api_key_2)  # step 16
    await page.wait(2000)
    await page.set_step(17)
    await page.click(delete_api_key_confirm)  # step 17
    await page.wait(2000)
    await page.set_step(18)
    _hit_el = await page.pw.evaluate(
        "([x, y, exp]) => { const els = document.elementsFromPoint(x, y); for (const el of els) { const t = (el.textContent || '').trim(); if (t === exp) return t; } return els[0] ? (els[0].textContent || '').trim() : null; }",
        [531, 95, "Secret API Keys"]
    )
    assert _hit_el is not None, "step 18: text_matched — no element at bbox center"
    assert _hit_el == "Secret API Keys", f"step 18: text_matched — expected \"Secret API Keys\", got {_hit_el!r}"
    await page.click(secret_api_keys)  # step 18
    await page.wait(2000)


if __name__ == "__main__":
    scenario.run()
