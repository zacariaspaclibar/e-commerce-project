from locators.loginPageLocators import LoginPageLocators


class LoginPage:
    def __init__(self,page):
        self.page = page
        self.loginLocators = LoginPageLocators(page)

    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client',wait_until="domcontentloaded",
    timeout=60000
)

    def register(self):
        self.loginLocators.register_btn.click()

    def dont_have_account(self):
        self.loginLocators.dont_have_an_account_btn.click()

    def registration_entry_point(self,entry_point):
        if entry_point == "Register":
            self.register()
        elif entry_point == "Don't have an account?":
            self.dont_have_account()