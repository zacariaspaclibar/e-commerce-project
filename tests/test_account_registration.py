import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from config.settings import TEST_USER_EMAIL,TEST_USER_PASSWORD,FIRST_NAME,LAST_NAME,TEST_CONFIRMED_PASSWORD,PHONE_NUMBER
from data import test_data

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
        FIRST_NAME,
        LAST_NAME,
        test_data.generated_email(),
        PHONE_NUMBER,
        TEST_USER_PASSWORD,
        TEST_CONFIRMED_PASSWORD
    )
    register_page.verify_registration_success()


def test_email_already_exist(browser_init):
    login_page = LoginPage(browser_init)
    register_page = RegisterPage(browser_init)

    login_page.navigate()
    login_page.register()

    register_page.account_registration(
        FIRST_NAME,
        LAST_NAME,
        TEST_USER_EMAIL,
        PHONE_NUMBER,
        TEST_USER_PASSWORD,
        TEST_CONFIRMED_PASSWORD
    )
    register_page.verify_email_exist()

def test_password_not_match(browser_init):
    login_page = LoginPage(browser_init)
    login_page.navigate()
    register_page = RegisterPage(browser_init)
    login_page.register()
    register_page.account_registration(
        FIRST_NAME,
        LAST_NAME,
        TEST_USER_EMAIL,
        PHONE_NUMBER,
        test_data.generate_password(),
        TEST_CONFIRMED_PASSWORD
    )
    register_page.verify_password_mismatch()

def test_registration_empty_field(browser_init):
    login_page = LoginPage(browser_init)
    register_page = RegisterPage(browser_init)

    login_page.navigate()
    login_page.register()
    register_page.registration_empty_field()





