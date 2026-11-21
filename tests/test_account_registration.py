import pytest

from config.settings import (
    FIRST_NAME,
    LAST_NAME,
    PHONE_NUMBER,
    TEST_CONFIRMED_PASSWORD,
    TEST_USER_EMAIL,
    TEST_USER_PASSWORD,
)
from data import test_data
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@pytest.mark.parametrize(
    "entry_point",
    [
        "Register",
        "Don't have an account?"
    ]
)
def test_account_successfully_register(page,entry_point):
    login_page = LoginPage(page)
    register_page = RegisterPage(page)
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


def test_email_already_exist(page):
    login_page = LoginPage(page)
    register_page = RegisterPage(page)

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

def test_password_not_match(page):
    login_page = LoginPage(page)
    login_page.navigate()
    register_page = RegisterPage(page)
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

def test_registration_empty_field(page):
    login_page = LoginPage(page)
    register_page = RegisterPage(page)

    login_page.navigate()
    login_page.register()
    register_page.registration_empty_field()





