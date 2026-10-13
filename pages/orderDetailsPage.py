from playwright.sync_api import Page, expect



class OrderDetailsPage:
    def __init__(self,page:Page):
        self.page = page
        # Text
        self.thank_you_banner = page.get_by_text(' Thankyou for the order. ')

        self.order_id = page.locator('td.em-spacer-1').locator('label.ng-star-inserted')

        self.order_name = page.locator('td.line-item.product-info-column.m-3').locator('div.title')
        
        
    def verify_order_in_cart_match(self,checkout_products):
        for i in range(self.order_id.count()):
            if checkout_products[i]['name'] == self.order_name.nth(i).text_content().replace('|','').strip():
                expect(self.order_name.nth(i)).to_be_visible()
                expect(self.thank_you_banner).to_be_visible()