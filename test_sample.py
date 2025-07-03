from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com")
        page.wait_for_load_state("load")
        title = page.title()
        assert "Google" in title, f"Expected 'Google' in title, but got '{title}'"
        print("Page title:", title)
        browser.close()