from playwright.sync_api import Page, expect

from locators.orderDetailsLocator import OrderDetailsLocators


class OrderDetailsPage:
    def __init__(self,page:Page):
        self.page = page
        self.order_details_locators = OrderDetailsLocators(self.page)
        
    def verify_order_in_cart_match(self,checkout_products):
        for i in range(self.order_details_locators.order_id.count()):
            if checkout_products[i]['name'] == self.order_details_locators.order_name.nth(i).text_content().replace('|','').strip():
                expect(self.order_details_locators.order_name.nth(i)).to_be_visible()
                expect(self.order_details_locators.thank_you_banner).to_be_visible()