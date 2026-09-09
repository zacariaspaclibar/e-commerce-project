from pages.registerPage import RegisterPage
from data import credentials


def test_account_successfully_register(browser_init):
    register_page = RegisterPage(browser_init)
    register_page.account_registration(
        credentials.FIRSTNAME,
        credentials.LASTNAME,
        credentials.EMAIL,
        credentials.PHONE_NUMBER,
        credentials.PASSWORD,
        credentials.CONFIRM_PASSWORD
    )
    register_page.successully_register()


def test_email_already_exist(browser_init):
    register_page = RegisterPage(browser_init)
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
    register_page = RegisterPage(browser_init)
    register_page.account_registration(
        credentials.FIRSTNAME,
        credentials.LASTNAME,
        credentials.EMAIL,
        credentials.PHONE_NUMBER,
        credentials.PASSWORD,
        credentials.INCORRECT_CONFIRM_PASSWORD
    )
    register_page.password_unmatch()

def test_empty_field(browser_init):
    register_page = RegisterPage(browser_init)
    register_page.empty_field()





