from playwright.sync_api import Page, expect
from pages.home_page import HomePage
import re


class CartPage:
    def __init__(self,page:Page):
        self.page = page
        self.home_page = HomePage(self.page)
        
    # self.continue_shopping_btn = page.get_by_role('button',name='Continue Shopping')
        self.buy_now_btn = page.get_by_role('button',name='Buy Now')
        self.delete_btn = page.locator('button.btn.btn-danger')
        self.checkout_btn = page.get_by_role('button',name='Checkout')

        # text
        self.total = (
            page.locator("li.totalRow")
            .filter(has=page.locator("span.label", has_text=re.compile(r"^Total$")))
            .locator("span.value")
            )
        
        self.subtotal = (
            page.locator("li.totalRow")
            .filter(has=page.locator('span.label', has_text=re.compile(r'^Subtotal$')))
            .locator("span.value")
            )
            
        #Banner
        self.no_product_banner = page.get_by_text('No Product in Your Cart')
        
        #cart card
        self.cart_card = page.locator('div.infoWrap')
        self.cart_product_id = page.locator('div.cartSection').locator('p.itemNumber')
        self.cart_product_name = page.locator('div.cartSection').locator('h3')
        
    def verify_delete_cart_items(self):
        while self.cart_card.count() > 0 :
            self.delete_btn.first.click()
        expect(self.no_product_banner).to_be_visible()
    
    def get_the_product_id(self, products):
        product_with_id = products
        for i in range(self.cart_card.count()):
            cart_product_id = self.cart_product_id.nth(i).text_content().replace('#','').strip()
            cart_product_name = self.cart_product_name.nth(i).text_content().strip()
            if products[i]['name'] == cart_product_name:
                products[i]['id'] = cart_product_id
        return product_with_id
        
    def verify_order_in_cart(self,products):
        order_count = self.cart_card.count()
        for i in range(order_count):
            if (
                products[i]['name'] == self.cart_product_name.nth(i).text_content().strip()
            ):
                return self.get_total_amount(products)
    
    def get_total_amount(self,products):
        total_cart_amount = 0
        for i in range(self.cart_card.count()):
            total_cart_amount += int(products[i]['price'])
        return total_cart_amount
        
    def product_checkout(self,products):
        products = self.get_the_product_id(products)
        total_cart_amount = self.verify_order_in_cart(products)
        if (
            total_cart_amount == int(self.total.text_content().replace('$','').strip()) 
            and 
            total_cart_amount == int(self.subtotal.text_content().replace('$','').strip())
        ):
            self.checkout_btn.click()
        return products
    