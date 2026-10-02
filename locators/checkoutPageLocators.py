from playwright.sync_api import Page


class CheckoutPageLocators:
    def __init__(self,page:Page):
        #Buttons
        self.place_order_btn = page.get_by_text('Place Order ')
        self.country_name_btn = page.locator('button.list-group-item.ng-star-inserted')

        #Fields 
        self.country_field = page.get_by_placeholder('Select Country')
        
        #Products
        self.checkout_product_name = page.locator('div.item__details').locator('div.item__title')
        self.checkout_product_price = page.locator('div.item__details').locator('div.item__price')
        
        
        # 6960eae1c941646b7a8b3ed3
        # 6abf6a5c2be7a4bc2b828ef2 