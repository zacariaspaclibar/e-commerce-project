from playwright.async_api import expect

from locators.homePageLocators import HomePageLocators


class HomePage:
    def __init__(self,page):
        self.page = page
        self.home_page_locators = HomePageLocators(self.page)

    def verify_green_banner(self):
        self.home_page_locators.blinking_green_btn.click()
        expect(self.page).to_have_title("QA Career Accelerator | Get Hired in 90 Days | Rahul Shetty")        