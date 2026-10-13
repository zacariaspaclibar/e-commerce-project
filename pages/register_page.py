from playwright.sync_api import expect

class RegisterPage:
    def __init__(self,page):
        self.page = page
        # Alert
        self.error_alert = page.get_by_text("User already exisits with")
        self.success_alert = page.get_by_text("Registered Successfully")
        
        #Heading
        self.account_successfully_created_text = page.get_by_role("heading", name="Account Created Successfully")

        # Buttons
        self.register_page_btn = page.get_by_role('button',name='Register')
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

        #Required field - Error message
        self.password_not_match_text = page.get_by_text("Password and Confirm Password must match with each other.")
        self.first_name_required_text = page.get_by_text("*First Name is required")
        self.email_required_text = page.get_by_text("*Email is required")
        self.phone_number_required_text = page.get_by_text("*Phone Number is required")
        self.password_required_text = page.get_by_text("*Password is required")
        self.confirm_password_required_text = page.get_by_text("Confirm Password is required")
        self.checkbox_required_text = page.get_by_text("*Please check above checkbox")

# FILLING UP THE REGISTRATION FORM
    def register_user_fields(self, first_name, last_name, email, phone, password, confirm_password):
        self.firstName_field.fill(first_name)
        self.lastName_field.fill(last_name)
        self.email_field.fill(email)
        self.phone_field.fill(phone)
        self.occupation.select_option("2: Student")
        self.gender.check()
        self.password_field.fill(password)
        self.confirm_password_field.fill(confirm_password)

# Expect - Messages for the scenarios
    def verify_registration_success(self):
            expect(self.success_alert).to_be_visible()
            expect(self.account_successfully_created_text).to_be_visible()

    def verify_email_exist(self):
         expect(self.error_alert).to_be_visible()

    def verify_password_mismatch(self):
         expect(self.password_not_match_text).to_be_visible()

    def verify_registration_required_field_error(self):
        expect(self.first_name_required_text).to_be_visible()
        expect(self.email_required_text).to_be_visible()
        expect(self.phone_number_required_text).to_be_visible()
        expect(self.password_required_text).to_be_visible()
        expect(self.confirm_password_required_text).to_be_visible()
        expect(self.checkbox_required_text).to_be_visible()
          
# Registration flow
    def account_registration(self,first_name, last_name, email, phone, password, confirm_password):
        self.register_user_fields(first_name, last_name, email, phone, password, confirm_password)
        self.age_checkbox.click()
        self.register_page_btn.click()
        
# No fields are filled up        
    def registration_empty_field(self):
        self.register_page_btn.click()
        self.verify_registration_required_field_error()