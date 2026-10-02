from playwright.sync_api import Page

from locators.checkoutPageLocators import CheckoutPageLocators

class CheckoutPage:
    def __init__(self,page:Page):
        self.page = page
        self. checkout_page_locators = CheckoutPageLocators(self.page)
        
        