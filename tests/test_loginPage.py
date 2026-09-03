from playwright.sync_api import Playwright

from locators.loginPageLocators import LoginPageLocators

def test_register_button(playwright: Playwright,browser_init):
    browser_init.goto(url='https://rahulshettyacademy.com/client/#/auth/login')
    login_locators = LoginPageLocators(browser_init)
    login_locators.register_btn.click()
    

