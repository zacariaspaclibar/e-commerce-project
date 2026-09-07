from data import credentials
from locators.registerPageLocators import RegisterPageLocators
from pages.loginPage import LoginPage
from playwright.sync_api import expect



def test_account_successfully_register(browser_init):
    loginPage = LoginPage(browser_init)
    loginPage.navigate()

    registerLocators = RegisterPageLocators(browser_init)
    registerLocators.register_btn.click()
    registerLocators.firstName_field.fill(credentials.FIRSTNAME)
    registerLocators.lastName_field.fill(credentials.LASTNAME)
    registerLocators.email_field.fill(credentials.EMAIL)
    registerLocators.phone_field.fill(credentials.PHONE_NUMBER)
    registerLocators.occupation.select_option("2: Student")
    registerLocators.gender.check()
    registerLocators.password_field.fill(credentials.PASSWORD)
    registerLocators.confirm_password_field.fill(credentials.CONFIRM_PASSWORD)
    registerLocators.age_checkbox.click()
    registerLocators.register_page_btn.click()
    expect(registerLocators.success_alert).to_be_visible()
    expect(registerLocators.account_successfully_created_text).to_be_visible()


def test_email_already_exist(browser_init):
    loginPage = LoginPage(browser_init)
    loginPage.navigate()
    registerLocators = RegisterPageLocators(browser_init)
    registerLocators.register_btn.click()
    registerLocators.firstName_field.fill(credentials.FIRSTNAME)
    registerLocators.lastName_field.fill(credentials.LASTNAME)
    registerLocators.email_field.fill(credentials.EXISTING_EMAIL)
    registerLocators.phone_field.fill(credentials.PHONE_NUMBER)
    registerLocators.occupation.select_option("2: Student")
    registerLocators.gender.check()
    registerLocators.password_field.fill(credentials.PASSWORD)
    registerLocators.confirm_password_field.fill(credentials.CONFIRM_PASSWORD)
    registerLocators.age_checkbox.click()
    registerLocators.register_page_btn.click()
    expect(registerLocators.error_alert).to_be_visible()

def test_password_not_match(browser_init):
    loginPage = LoginPage(browser_init)
    loginPage.navigate()
    registerLocators = RegisterPageLocators(browser_init)
    registerLocators.register_btn.click()
    registerLocators.firstName_field.fill(credentials.FIRSTNAME)
    registerLocators.lastName_field.fill(credentials.LASTNAME)
    registerLocators.email_field.fill(credentials.EMAIL)
    registerLocators.phone_field.fill(credentials.PHONE_NUMBER)
    registerLocators.occupation.select_option("2: Student")
    registerLocators.gender.check()
    registerLocators.password_field.fill(credentials.PASSWORD)
    registerLocators.confirm_password_field.fill(credentials.INCORRECT_CONFIRM_PASSWORD)
    registerLocators.age_checkbox.click()
    registerLocators.register_page_btn.click()
    expect(registerLocators.password_not_match_text).to_be_visible()

def test_empty_field(browser_init):
    loginPage = LoginPage(browser_init)
    loginPage.navigate()
    registerLocators = RegisterPageLocators(browser_init)
    registerLocators.register_btn.click()
    registerLocators.register_page_btn.click()
    expect(registerLocators.first_name_required_text).to_be_visible()
    expect(registerLocators.email_required_text).to_be_visible()
    expect(registerLocators.phone_number_required_text).to_be_visible()
    expect(registerLocators.password_required_text).to_be_visible()
    expect(registerLocators.confirm_password_required_text).to_be_visible()
    expect(registerLocators.checkbox_required_text).to_be_visible()





