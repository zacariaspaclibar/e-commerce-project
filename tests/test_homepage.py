
import pytest

from pages.Homepage import HomePage
from pages.loginPage import LoginPage
from data import credentials

@pytest.mark.parametrize("username,password",[(credentials.EXISTING_EMAIL, credentials.PASSWORD)])
def test_green_banner(browser_init,username,password):
    login_page = LoginPage(browser_init)
    login_page.navigate()
    login_page.account_login(username,password)
    home_page = HomePage(browser_init)
    home_page.verify_green_banner()