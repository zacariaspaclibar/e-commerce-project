from playwright.sync_api import Page
class RegisterPageLocator:
    def __init__(self,page:Page):
        # Buttons
        self.register_btn = page.get_by_role('link',name='Register')
        self.register_page_btn = page.get_by_role('button',name='Register')
        self.dont_have_an_account_btn = page.get_by_text("Don't have an account?")
        self.already_have_account_btn = page.get_by_role('link',name='Already have an account? Login here')


        # Fields
        self.firstName_field = page.get_by_placeholder('First Name')
        self.lastName_field = page.get_by_placeholder('Last Name')
        self.email_field = page.get_by_placeholder('email@example.com')
        self.phone_field = page.get_by_placeholder('enter your number')
        self.password_field = page.get_by_placeholder('Passsword')
        self.confirm_password_field = page.get_by_placeholder('Confirm Passsword')
        self.age_field = page.get_by_role('checkbox',name=' I am 18 year or Older ')

