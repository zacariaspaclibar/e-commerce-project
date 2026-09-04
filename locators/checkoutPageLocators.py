from playwright.sync_api import Page


class CheckoutPageLocators:
    def __init__(self,page:Page):
        #Buttons
        self.place_order_btn = page.get_by_role('button',name='Place Order ')

        #Fields 
        self.country_field = page.get_by_placeholder('Select Country')