from playwright.sync_api import Page


class OrderDetailsLocators:
    def __init__(self,page:Page):
        # Text
        self.thank_you_banner = page.get_by_text(' Thankyou for the order. ')