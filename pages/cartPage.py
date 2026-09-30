from playwright.sync_api import Page, expect

from locators.cartPageLocators import CartPageLocators
from locators.homePageLocators import HomePageLocators


class CartPage:
    def __init__(self,page:Page):
        self.page = page
        self.cart_page_locators = CartPageLocators(self.page)
        self.home_page_locators = HomePageLocators(self.page)
        
    def verify_delete_cart_items(self):
        self.home_page_locators.cart_btn.nth(0).click()
        while self.cart_page_locators.cart_card.count() > 0 :
            self.cart_page_locators.delete_btn.first.click()
        expect(self.cart_page_locators.no_product_banner).to_be_visible()
        
    # TODO: Add test case for product order , 
    # copy the product dictionary then append product id
    # fill the country field then get the product id match it in the success order page
    