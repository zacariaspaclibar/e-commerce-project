from playwright.sync_api import Page
class LoginPageLocators:
    def __init__(self,page:Page):
        # Buttons
        self.login_btn = page.get_by_role('button',name='Login')
        
        self.register_btn = page.get_by_role('link',name='Register')
        self.dont_have_an_account_btn = page.get_by_text("Don't have an account?")
        
        #Fields 
        self.email_field = page.get_by_role('textbox',name='email@example.com')
        self.password_field = page.get_by_role('textbox',name='enter your passsword')
        
        # validations
        self.alert_login_success = page.get_by_text('Login Successfully')
        self.alert_login_failed = page.get_by_text('Incorrect email or password.')
        
        self.username_required_message = page.get_by_text('*Email is required')
        self.password_required_message = page.get_by_text('*Password is required')