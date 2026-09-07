
from playwright.sync_api import Page


class RegisterPageLocators:
    def __init__(self,page:Page):
         # Alert
        self.success_alert = page.get_by_text("Registered Successfully")
        self.error_alert = page.get_by_role("alert", name="User already exisits with")
        
        #Heading
        self.account_successfully_created_text = page.get_by_role("heading", name="Account Created Successfully")

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
        self.password_field = page.get_by_role("textbox", name="Passsword")
        self.confirm_password_field = page.get_by_placeholder('Confirm Passsword')
        
        #Checkbox
        self.age_checkbox = page.locator(".col-md-1")
        self.occupation = page.get_by_role("combobox")
        self.gender = page.get_by_role("radio", name="Male", exact=True)

       