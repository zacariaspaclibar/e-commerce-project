

from playwright.sync_api import Page
import re


class CartPageLocators:
    def __init__(self,page:Page):
        self.continue_shopping_btn = page.get_by_role('button',name='Continue Shopping')
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