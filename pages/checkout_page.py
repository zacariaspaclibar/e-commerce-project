from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self,page:Page):
        self.page = page
        #Buttons
        self.place_order_btn = page.get_by_text('Place Order ')
        self.country_name_btn = page.locator('button.list-group-item.ng-star-inserted')

        #Fields 
        self.country_field = page.get_by_placeholder('Select Country')
        
        #Products
        self.checkout_product_name = page.locator('div.item__details').locator('div.item__title')
        self.checkout_product_price = page.locator('div.item__details').locator('div.item__price')
        
    def fill_shipping_info(self,country):        
        self.country_field.click()
        self.country_field.press_sequentially(country)
        expect(self.country_name_btn).to_be_visible()
        self.country_name_btn.click()
        self.place_order_btn.click()