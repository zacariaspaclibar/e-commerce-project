from playwright.sync_api import expect

from data import credentials
from locators.loginPageLocators import LoginPageLocators


class LoginPage:
    def __init__(self,page):
        self.page = page
        self.loginLocators = LoginPageLocators(page)

    def navigate(self):
        self.page.goto(credentials.BASED_URL,wait_until="domcontentloaded", timeout=60000)

    def register(self):
        self.loginLocators.register_btn.click()

    def dont_have_account(self):
        self.loginLocators.dont_have_an_account_btn.click()

    def registration_entry_point(self,entry_point):
        if entry_point == "Register":
            self.register()
        elif entry_point == "Don't have an account?":
            self.dont_have_account()
            
    
    def verify_login_success(self,status):
            if status:
                expect(self.loginLocators.alert_login_success).to_be_visible()
            else:
                expect(self.loginLocators.alert_login_failed).to_be_visible()
    
    
    def verify_login_empty_field(self):
            expect(self.loginLocators.username_required_message).to_be_visible()
            expect(self.loginLocators.password_required_message).to_be_visible()
    
    
    def account_login(self,username,password):
        self.loginLocators.email_field.fill(username)
        self.loginLocators.password_field.fill(password)
        self.loginLocators.login_btn.click()
    
    def login_empty_field(self):
        self.loginLocators.login_btn.click()
        self.verify_login_empty_field()