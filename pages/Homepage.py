from playwright.sync_api import expect

from locators.homePageLocators import HomePageLocators


class HomePage:
    def __init__(self,page):
        self.page = page
        self.home_page_locators = HomePageLocators(self.page)

    def verify_green_banner(self):
        with self.page.context.expect_page() as new_page:
            self.home_page_locators.blinking_green_btn.click()
        new_tab = new_page.value
        new_tab.wait_for_load_state()
        header = new_tab.get_by_text('From QA Learner to Hired Professional in 90 Days')
        expect(header).to_be_visible()