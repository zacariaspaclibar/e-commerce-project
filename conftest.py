from playwright.sync_api import Playwright
import pytest

from api.apiUtils import APIUTILS
from data import credentials

@pytest.fixture
def browser_init(playwright:Playwright):
    browser = playwright.chromium.launch(headless= False, slow_mo = 1000)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    
@pytest.fixture    
def auth_token(playwright:Playwright):
    api_utils = APIUTILS()
    
    return api_utils.api_token(
        credentials.EXISTING_EMAIL,
        credentials.PASSWORD,
        playwright
    )

@pytest.fixture
def authenticated_page(browser_init,auth_token):
    browser_init.add_init_script(
        f"window.localStorage.setItem('token', '{auth_token}')"
    )
    browser_init.goto(credentials.BASED_URL)
    
    return browser_init