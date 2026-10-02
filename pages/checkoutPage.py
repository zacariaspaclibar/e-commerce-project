from playwright.sync_api import Page, expect

from locators.checkoutPageLocators import CheckoutPageLocators

class CheckoutPage:
    def __init__(self,page:Page):
        self.page = page
        self. checkout_page_locators = CheckoutPageLocators(self.page)
        
    def fill_shipping_info(self,country):        
        self.checkout_page_locators.country_field.click()
        self.checkout_page_locators.country_field.press_sequentially(country)
        expect(self.checkout_page_locators.country_name_btn).to_be_visible()
        self.checkout_page_locators.country_name_btn.click()
        self.checkout_page_locators.place_order_btn.click()