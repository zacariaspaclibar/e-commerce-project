import pytest
from playwright.sync_api import Playwright

from api.api_utils import ApiUtils
from config.settings import BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD

# @pytest.fixture
# def browser_init(playwright:Playwright):
#     browser = playwright.chromium.launch(headless= False, slow_mo = 1000)
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     context.close()
#     browser.close()
    
@pytest.fixture    
def auth_token(playwright:Playwright):
    api_utils = ApiUtils()
    
    return api_utils.api_token(
        TEST_USER_EMAIL,
        TEST_USER_PASSWORD,
        playwright
    )

@pytest.fixture
def authenticated_page(page,auth_token):
    page.add_init_script(
        f"window.localStorage.setItem('token', '{auth_token}')"
    )
    page.goto(BASE_URL)
    
    return page