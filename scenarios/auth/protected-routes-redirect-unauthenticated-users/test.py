#!/usr/bin/env python3
"""auth.protected-routes-redirect-unauthenticated-users

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="auth.protected-routes-redirect-unauthenticated-users",
    base_url="http://localhost:19000/app",
    viewport_width=1920,
    viewport_height=1080,
    wait_ms=2000,
)


@scenario.test
async def test(page: Page):
    await page.set_step(1)
    await page.goto("/orders")  # step 1
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/login*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 1: url_match /login — " + str(_e)) from _e
    await page.set_step(2)
    await page.goto("/products")  # step 2
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/login*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 2: url_match /login — " + str(_e)) from _e
    await page.set_step(3)
    await page.goto("/settings/store")  # step 3
    await page.wait(2000)
    try:
        await page.pw.wait_for_url("**/login*", timeout=5000)
    except Exception as _e:
        raise AssertionError("step 3: url_match /login — " + str(_e)) from _e


if __name__ == "__main__":
    scenario.run()
