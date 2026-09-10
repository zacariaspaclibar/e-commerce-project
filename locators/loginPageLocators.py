from playwright.sync_api import Page
class LoginPageLocators:
    def __init__(self,page):
        # Buttons
        self.login_btn = page.get_by_role('button',name='Login')
        
        self.register_btn = page.get_by_role('link',name='Register')
        self.dont_have_an_account_btn = page.get_by_text("Don't have an account?")
        
        #Fields 
        self.email_field = page.get_by_role('textbox',name='email@example.com')
        self.password_field = page.get_by_role('textbox',name='enter your passsword')