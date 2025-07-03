import re
import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv('.env', override=True)
url = os.getenv("url")

def test_google_title(page):
    page.goto(url)
    expect(page).to_have_title(re.compile("Google"))
    print("Page title:", page.title())
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))
    print("Search results page title:", page.title())