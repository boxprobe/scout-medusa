#!/usr/bin/env python3
"""inventory.inventory-search-and-filter

Auto-generated scenario — bbox coordinates are runtime-resolved; do not edit manually
"""
from scout.runner import Locator, Page, Scenario

scenario = Scenario(
    name="inventory.inventory-search-and-filter",
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
add_filter = Locator(
    name="add-filter", tag="button",
    bbox=(299, 163, 73, 28),
    scroll_y=0,
    pos_type="abs",
)
sku_option = Locator(
    name="sku-option", tag="div",
    bbox=(303, 267, 277, 32),
    scroll_y=0,
    pos_type="abs",
)
sku_input = Locator(
    name="sku-input", tag="input",
    bbox=(311, 241, 276, 28),
    scroll_y=0,
    pos_type="abs",
)
filter_result = Locator(
    name="filter-result", tag="div",
    bbox=(715, 256, 347, 47),
    scroll_y=0,
    pos_type="abs",
)
clear_filer = Locator(
    name="clear-filer", tag="button",
    bbox=(498, 163, 23, 28),
    scroll_y=0,
    pos_type="abs",
)
search_text = Locator(
    name="search-text", tag="input",
    bbox=(1609, 163, 182, 28),
    scroll_y=0,
    pos_type="abs",
)
search_result = Locator(
    name="search-result", tag="div",
    bbox=(716, 256, 346, 47),
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
    await page.click(add_filter)  # step 6
    await page.wait(2000)
    await page.set_step(7)
    await page.click(sku_option)  # step 7
    await page.wait(2000)
    await page.set_step(8)
    await page.fill(sku_input, "SWEATSHIRT-XL")  # step 8
    await page.wait(2000)
    await page.set_step(10)
    await page.click(clear_filer)  # step 10
    await page.wait(2000)
    await page.set_step(11)
    await page.fill(search_text, "SHIRT-L-BLACK")  # step 11
    await page.wait(2000)


if __name__ == "__main__":
    scenario.run()
