from playwright.sync_api import Page

from locators.cartPageLocators import CartPageLocators


class CartPage:
    def __init__(self,page:Page):
        self.page = page
        self.cart_Page_Locator = CartPageLocators(self.page)