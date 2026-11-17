import pytest
from data import test_data
from pages.login_page import LoginPage
from config.settings import TEST_USER_EMAIL,TEST_USER_PASSWORD

@pytest.mark.parametrize(
        "username,password,status", [
            (TEST_USER_EMAIL,TEST_USER_PASSWORD,True),
            (TEST_USER_EMAIL,test_data.generate_password(),False),
            (test_data.generated_email(),TEST_USER_PASSWORD,False)
        ]
        )
def test_login_successfully(browser_init,username,password,status):
    login_page = LoginPage(browser_init)
    login_page.navigate()
    login_page.account_login(username,password)
    login_page.verify_login_status(status)

def test_login_empty_field(browser_init):
    login_page = LoginPage(browser_init)
    login_page.navigate()
    login_page.login_empty_field()