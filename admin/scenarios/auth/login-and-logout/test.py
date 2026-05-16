#!/usr/bin/env python3
"""auth.login-and-logout

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="auth.login-and-logout",
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
where_html_dir_ltr_where_data_son = Locator(
    name="where-html-dir-ltr-where-data-son", tag="button",
    bbox=(12, 1036, 195, 32),
    scroll_y=0,
    pos_type="abs",
)
log_out = Locator(
    name="log-out", tag="div",
    bbox=(16, 992, 187, 32),
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
    try:
        await page.pw.wait_for_url("**/orders*", timeout=1000)
    except Exception as _e:
        raise AssertionError("step 4: url_match /orders — " + str(_e)) from _e
    await page.set_step(5)
    await page.click(where_html_dir_ltr_where_data_son)  # step 5
    await page.wait(2000)
    await page.set_step(6)
    await page.click(log_out)  # step 6
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/login*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 6: url_match /login — " + str(_e)) from _e


if __name__ == "__main__":
    scenario.run()
