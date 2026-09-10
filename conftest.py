from playwright.sync_api import Playwright
import pytest

@pytest.fixture
def browser_init(playwright:Playwright):
    browser = playwright.chromium.launch(headless= False, slow_mo = 1000)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()