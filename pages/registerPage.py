from playwright.sync_api import expect
from locators.registerPageLocators import RegisterPageLocators
from pages.loginPage import LoginPage

class RegisterPage:
    def __init__(self,page):
        self.page = page
        self.loginPage = LoginPage(self.page)
        self.registerLocators = RegisterPageLocators(self.page)
        
    def register_user_fields(self, first_name, last_name, email, phone, password, confirm_password):
        self.registerLocators.firstName_field.fill(first_name)
        self.registerLocators.lastName_field.fill(last_name)
        self.registerLocators.email_field.fill(email)
        self.registerLocators.phone_field.fill(phone)
        self.registerLocators.occupation.select_option("2: Student")
        self.registerLocators.gender.check()
        self.registerLocators.password_field.fill(password)
        self.registerLocators.confirm_password_field.fill(confirm_password)

    def successully_register(self):
            expect(self.registerLocators.success_alert).to_be_visible()
            expect(self.registerLocators.account_successfully_created_text).to_be_visible()

    def email_exist_error(self):
         expect(self.registerLocators.error_alert).to_be_visible()

    def password_unmatch(self):
         expect(self.registerLocators.password_not_match_text).to_be_visible()

    def empty_field_error(self):
        expect(self.registerLocators.first_name_required_text).to_be_visible()
        expect(self.registerLocators.email_required_text).to_be_visible()
        expect(self.registerLocators.phone_number_required_text).to_be_visible()
        expect(self.registerLocators.password_required_text).to_be_visible()
        expect(self.registerLocators.confirm_password_required_text).to_be_visible()
        expect(self.registerLocators.checkbox_required_text).to_be_visible()
          

    def account_registration(self,first_name, last_name, email, phone, password, confirm_password):
        self.loginPage.navigate()
        self.registerLocators.register_btn.click()
        self.register_user_fields(first_name, last_name, email, phone, password, confirm_password)
        self.registerLocators.age_checkbox.click()
        self.registerLocators.register_page_btn.click()
        
    def empty_field(self):
        self.loginPage.navigate()
        self.registerLocators.register_btn.click()
        self.registerLocators.register_page_btn.click()
        self.empty_field_error()