import pytest
from data import credentials
from pages.loginPage import LoginPage

@pytest.mark.parametrize(
        "username,password,status", [
            (credentials.EXISTING_EMAIL,credentials.PASSWORD,True),
            (credentials.EXISTING_EMAIL,credentials.generate_password(),False),
            (credentials.generated_email(),credentials.PASSWORD,False)
        ]
        )
def test_login_successfully(browser_init,username,password,status):
    login_page = LoginPage(browser_init)
    login_page.navigate()
    login_page.account_login(username,password)
    login_page.verify_login_success(status)

def test_login_empty_field(browser_init):
    login_page = LoginPage(browser_init)
    login_page.navigate()
    login_page.login_empty_field()