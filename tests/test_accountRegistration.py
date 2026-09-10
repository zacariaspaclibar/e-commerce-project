import pytest
from pages.loginPage import LoginPage
from pages.registerPage import RegisterPage
from data import credentials

@pytest.mark.parametrize(
    "entry_point",
    [
        "Register",
        "Don't have an account?"
    ]
)
def test_account_successfully_register(browser_init,entry_point):
    login_page = LoginPage(browser_init)
    register_page = RegisterPage(browser_init)
    login_page.navigate()
    login_page.registration_entry_point(entry_point)
    register_page.account_registration(
        credentials.FIRSTNAME,
        credentials.LASTNAME,
        credentials.generated_email(),
        credentials.PHONE_NUMBER,
        credentials.PASSWORD,
        credentials.CONFIRM_PASSWORD
    )
    register_page.successully_register()


def test_email_already_exist(browser_init):
    login_page = LoginPage(browser_init)
    register_page = RegisterPage(browser_init)

    login_page.navigate()
    login_page.register()

    register_page.account_registration(
        credentials.FIRSTNAME,
        credentials.LASTNAME,
        credentials.EXISTING_EMAIL,
        credentials.PHONE_NUMBER,
        credentials.PASSWORD,
        credentials.CONFIRM_PASSWORD
    )
    register_page.email_exist_error()

def test_password_not_match(browser_init):
    login_page = LoginPage(browser_init)
    login_page.navigate()
    register_page = RegisterPage(browser_init)
    login_page.register()
    register_page.account_registration(
        credentials.FIRSTNAME,
        credentials.LASTNAME,
        credentials.generated_email(),
        credentials.PHONE_NUMBER,
        credentials.PASSWORD,
        credentials.INCORRECT_CONFIRM_PASSWORD
    )
    register_page.password_unmatch()

def test_empty_field(browser_init):
    login_page = LoginPage(browser_init)
    register_page = RegisterPage(browser_init)

    login_page.navigate()
    login_page.register()
    register_page.empty_field()





