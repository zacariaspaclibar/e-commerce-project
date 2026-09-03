from playwright.sync_api import Page
class RegisterPageLocator:
    def __init__(self,page:Page):
        # Buttons
        self.register_btn = page.get_by_role('link',name='Register')
        self.register_page_btn = page.get_by_role('button',name='Register')
        self.dont_have_an_account_btn = page.get_by_text("Don't have an account?")
        self.already_have_account_btn = page.get_by_role('link',name='Already have an account? Login here')


        # Fields
        self.firstName_field = page.get_by_role('textbox',name='First Name')
        self.lastName_field = page.get_by_role('textbox',name='Last Name')
        self.email_field = page.get_by_role('textbox',name='email@example.com')
        self.phone_field = page.get_by_role('textbox',name='enter your number')
        self.password_field = page.get_by_role('textbox',name='Passsword')
        self.confirm_password_field = page.get_by_role('textbox',name='Confirm Passsword')
        self.age_field = page.get_by_role('checkbox',name=' I am 18 year or Older ')

