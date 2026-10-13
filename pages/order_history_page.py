
from playwright.sync_api import expect

from api.api_utils import ApiUtils
from pages.home_page import HomePage


class OrderHistoryPage:
    def __init__(self,page):
        self.page = page
        self.home_page = HomePage(self.page)
        self.body = self.page.locator('body')
            
    def selected_order(self,order_id):
                self.page.locator('tr').filter(has_text=order_id).get_by_role('button', name='View').click()
    
    def get_order_id(self,token,playwright,country,product_id):
        api_utils = ApiUtils()
        return api_utils.order_id(token,playwright,country,product_id)
        
    def order_history(self,token,playwright,country,product_id):
        order_id = self.get_order_id(token,playwright,country,product_id)
        self.home_page.order_btn.click()
        self.selected_order(order_id)
        
    def verifyOrder(self):
        expect(self.body).to_contain_text('order summary')