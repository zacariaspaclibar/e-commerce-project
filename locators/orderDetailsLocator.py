from playwright.sync_api import Page


class OrderDetailsLocators:
    def __init__(self,page:Page):
        # Text
        self.thank_you_banner = page.get_by_text(' Thankyou for the order. ')
    
        self.order_id = page.locator('td.em-spacer-1').locator('label.ng-star-inserted')
        
        self.order_name = page.locator('td.line-item.product-info-column.m-3').locator('div.title')