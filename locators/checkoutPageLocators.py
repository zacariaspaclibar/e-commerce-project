from playwright.sync_api import Page


class CheckoutPageLocators:
    def __init__(self,page:Page):
        #Buttons
        self.place_order_btn = page.get_by_role('button',name='Place Order ')

        #Fields 
        self.country_field = page.get_by_placeholder('Select Country')
        
        #Products
        self.checkout_order_list = page.locator('div.col-md-5')
        self.checkout_product_name = page.locator('div.item__details').locator('div.item__title')
        self.checkout_product_price = page.locator('div.item__details').locator('div.item__price')
        