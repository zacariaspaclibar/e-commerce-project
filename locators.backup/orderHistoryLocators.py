

class OrderHistoryLocators:
    def __init__(self,page):
        self.page = page
        self.body = self.page.locator('body')
    
    def selected_order(self,order_id):
        self.page.locator('tr').filter(has_text=order_id).get_by_role('button', name='View').click()