from playwright.sync_api import expect
from locators.homePageLocators import HomePageLocators
import re

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
                    
    def filter_by_name(self,product_name):
        self.home_page_locators.search_field.fill(product_name)
        self.home_page_locators.search_field.press('Enter')
        text = self.home_page_locators.show_result.text_content()
        self.verify_product_exist(text)
    
    def filter_by_price(self,price_range_min,price_range_max):
        self.home_page_locators.min_price_range_field.fill(price_range_min)
        self.home_page_locators.max_price_range_field.fill(price_range_max)
        self.home_page_locators.max_price_range_field.press('Enter')
        text = self.home_page_locators.show_result.text_content()
        self.verify_product_exist(text)
        
    def verify_product_exist(self,text):
        count = re.search(r'\d+',text)
        result_count = int(count.group())
        if result_count > 0:
            expect(self.home_page_locators.show_result).to_have_text(f'Showing {result_count} results   | ')
        else: 
            expect(self.home_page_locators.error_product_not_found).to_be_visible()
            
        