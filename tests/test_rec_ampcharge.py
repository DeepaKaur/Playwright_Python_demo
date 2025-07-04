import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.ampol.com.au/")
    page.get_by_role("link", name="Your Vehicle").first.click()
    page.get_by_role("link", name="EV Charging", exact=True).click()
    page.get_by_role("link", name="Find a Charging Location").click()
    page.get_by_test_id("Input").locator("span").nth(2).click()
    page.locator("#rc_select_0").fill("Werrington")
    page.get_by_text("Werrington NSW", exact=True).click()
    page.get_by_role("heading", name="Ampol Foodary Werrington").click()
    expect(page.get_by_role("heading", name="Ampol Foodary Werrington")).to_be_visible()
    expect(page.locator("#page-content")).to_contain_text("Cnr Dunheved Rd & Henry Lawson Dr, Werrington, NSW, 2747")
