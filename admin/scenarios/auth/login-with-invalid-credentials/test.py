#!/usr/bin/env python3
"""auth.login-with-invalid-credentials

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="auth.login-with-invalid-credentials",
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

@scenario.test
async def test(page: Page):
    await page.set_step(1)
    await page.goto("/login")  # step 1
    await page.wait(2000)
    await page.set_step(2)
    await page.fill(email, "invalide@email.com")  # step 2
    await page.wait(2000)
    await page.set_step(3)
    await page.fill(password, "invalid-password")  # step 3
    await page.wait(2000)
    await page.set_step(4)
    await page.click(continue_with_email)  # step 4
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/login*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 4: url_match /login — " + str(_e)) from _e


if __name__ == "__main__":
    scenario.run()
