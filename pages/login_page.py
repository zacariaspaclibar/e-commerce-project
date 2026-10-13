from playwright.sync_api import expect

from data import credentials


class LoginPage:
    def __init__(self,page):
        self.page = page
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





    def navigate(self):
        self.page.goto(credentials.BASED_URL,wait_until="domcontentloaded", timeout=60000)

    def register(self):
        self.register_btn.click()

    def dont_have_account(self):
        self.dont_have_an_account_btn.click()

    def registration_entry_point(self,entry_point):
        if entry_point == "Register":
            self.register()
        elif entry_point == "Don't have an account?":
            self.dont_have_account()
            
    
    def verify_login_status(self,status):
            if status:
                expect(self.alert_login_success).to_be_visible()
            else:
                expect(self.alert_login_failed).to_be_visible()
    
    
    def verify_login_empty_field(self):
            expect(self.username_required_message).to_be_visible()
            expect(self.password_required_message).to_be_visible()
    
    
    def account_login(self,username,password):
        self.email_field.fill(username)
        self.password_field.fill(password)
        self.login_btn.click()
    
    def login_empty_field(self):
        self.login_btn.click()
        self.verify_login_empty_field()