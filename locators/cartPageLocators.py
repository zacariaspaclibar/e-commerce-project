

class CartPageLocators:
    def __init__(self,page):
        self.continue_shopping_btn = page.get_by_role('button',name='Continue Shopping')
        self.buy_now_btn = page.get_by_role('button',name='Buy Now')
        self.delete_btn = page.locator('.btn.btn-danger')
        self.checkout_btn = page.get_by_role('button',name='Checkout')

        # text
        self.total = (
    page.locator("li.totalRow")
    .filter(has=page.locator("span.label", has_text="Total"))
    .locator("span.value")
)
        self.subtotal = (
    page.locator("li.totalRow")
    .filter(has=page.locator("span.label", has_text="Subtotal"))
    .locator("span.value")
)
        
        #Banner
        self.no_product_banner = page.get_by_text('No Product in Your Cart')