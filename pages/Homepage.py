from playwright.async_api import Page, expect

from locators.homePageLocators import HomePageLocators


class HomePage:
    def __init__(self,page:Page):
        self.page = page
        self.home_page_locators = HomePageLocators(self.page)

    def verify_green_banner(self):
        with self.page.context.expect_page() as new_page:
            self.home_page_locators.blinking_green_btn.click()
            new_tab = new_page.value
            new_tab.wait_for_load_state()
            assert "QA Career Accelerator | Get Hired in 90 Days | Rahul Shetty" in new_tab.title()#working
            # expect(new_tab).to_have_title("QA Career Accelerator | Get Hired in 90 Days | Rahul Shetty") - now working 