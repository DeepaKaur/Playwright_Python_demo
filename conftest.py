import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for headless mode
        yield browser
        browser.close()
        
@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()