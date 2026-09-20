class HomePageLocators:
    def __init__(self,page):
        # Buttons
        self.blinking_green_btn = page.get_by_role('link',name= "🎯 I'll help you prepare for your next QA job — Explore the QA Career Accelerator.")
        self.view_btn = page.get_by_role('button',name=' View')
        self.add_to_cart_btn = page.get_by_role('button',name=' Add To Cart')
        self.cart_btn = page.get_by_role('button',name='  Cart ')
        self.order_btn = page.get_by_role('button',name='  ORDERS')

        #Fields
        self.search_field = page.get_by_role('textbox',name='search')
        self.min_price_range_field = page.get_by_role('textbox',name='Min Price')
        self.max_price_range_field = page.get_by_role('textbox',name='Max Price')

        #Error Message
        self.homepage_error_msg = page.get_by_label("No Products Found")

        #Successfully Login Message
        self.login_success_msg = page.get_by_label("Login Successfully")
        