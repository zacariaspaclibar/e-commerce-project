from playwright.sync_api import Page

from locators.orderDetailsLocator import OrderDetailsLocators


class OrderDetailsPage:
    def __init__(self,page:Page):
        self.page = page
        self.order_details_locators = OrderDetailsLocators(self.page)