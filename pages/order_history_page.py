
from playwright.sync_api import expect

from api.apiUtils import APIUTILS
from locators.homePageLocators import HomePageLocators
from locators.orderHistoryLocators import OrderHistoryLocators


class OrderHistoryPage:
    def __init__(self,page):
        self.page = page
        self.home_page_locators = HomePageLocators(self.page)
        self.order_history_locators = OrderHistoryLocators(self.page)
    
    def get_order_id(self,token,playwright,country,product_id):
        api_utils = APIUTILS()
        return api_utils.order_id(token,playwright,country,product_id)
        
    def order_history(self,token,playwright,country,product_id):
        order_id = self.get_order_id(token,playwright,country,product_id)
        self.home_page_locators.order_btn.click()
        self.order_history_locators.selected_order(order_id)
        
    def verifyOrder(self):
        expect(self.order_history_locators.body).to_contain_text('order summary')