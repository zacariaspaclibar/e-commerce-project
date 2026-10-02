from playwright.sync_api import Page, expect

from locators.cartPageLocators import CartPageLocators
from locators.homePageLocators import HomePageLocators
from pages.Homepage import HomePage


class CartPage:
    def __init__(self,page:Page):
        self.page = page
        self.cart_page_locators = CartPageLocators(self.page)
        self.home_page_locators = HomePageLocators(self.page)
        self.home_page = HomePage(self.page)
        
    def verify_delete_cart_items(self):
        while self.cart_page_locators.cart_card.count() > 0 :
            self.cart_page_locators.delete_btn.first.click()
        expect(self.cart_page_locators.no_product_banner).to_be_visible()
    
    def adding_product_id(self,products):
        for i in range(self.cart_page_locators.cart_card.count()):
            cart_product_id = self.cart_page_locators.cart_product_id.nth(i).text_content().replace('#','').strip()
            cart_product_name = self.cart_page_locators.cart_product_name.nth(i).text_content().strip()
            if products[i]['name'] == cart_product_name:
                products[i]['id'] = cart_product_id
    
    def get_total_amount(self,products):
        total_cart_amount = 0
        for i in range(self.cart_page_locators.cart_card.count()):
            total_cart_amount += int(products[i]['price'])
        return total_cart_amount
        
    def product_checkout(self,products):
        self.adding_product_id(products)
        total_cart_amount = self.get_total_amount(products)
        if (
            total_cart_amount == int(self.cart_page_locators.total.text_content().replace('$','').strip()) 
            and 
            total_cart_amount == int(self.cart_page_locators.subtotal.text_content().replace('$','').strip())
        ):
            self.cart_page_locators.checkout_btn.click()
        return products
    