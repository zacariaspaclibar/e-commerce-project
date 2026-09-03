from playwright.sync_api import Page
class LoginPageLocators:
    def __init__(self,page):
        self.email_field = page.get_by_placeholder('email@example.com')
        self.password_field = page.get_by_placeholder('enter your passsword')
        self.login_btn = page.get_by_role('button',name='Login')