from playwright.sync_api import expect
import re

class HomePage:
    def __init__(self,page):
        self.page = page
        # Buttons
        self.blinking_green_btn = page.get_by_role('link',name= "🎯 I'll help you prepare for your next QA job — Explore the QA Career Accelerator.")
        self.view_btn = page.get_by_role('button',name=' View').first
        self.add_to_cart_btn = page.get_by_role('button',name=' Add To Cart')
        self.product_add_to_cart_btn = page.get_by_role('button',name='Add to Cart')
        self.cart_btn = page.get_by_role('button', name='\xa0 Cart ')
        self.order_btn = page.get_by_role('button',name='  ORDERS')

        #Fields
        self.search_field = page.get_by_role('textbox',name='search')
        self.min_price_range_field = page.get_by_role('textbox',name='Min Price')
        self.max_price_range_field = page.get_by_role('textbox',name='Max Price')

        #Error Message
        self.error_product_not_found = page.get_by_label("No Products Found")
        
        #TEXT RESULT Messsage
        self.show_result = page.locator('div#res')

        #Successfully Login Message
        self.login_success_msg = page.get_by_label("Login Successfully")
        self.product_added_msg = page.get_by_text('Product Added To Cart')
        
        #Header
        self.product_card = page.locator('div.card-body')
        self.product_name = page.locator('div.card-body').locator('h5')
        self.product_price = page.locator('div.card-body').locator('div.text-muted')

    def verify_green_banner(self):
        with self.page.context.expect_page() as new_page:
            self.blinking_green_btn.click()
        new_tab = new_page.value
        new_tab.wait_for_load_state()
        header = new_tab.get_by_text('From QA Learner to Hired Professional in 90 Days')
        expect(header).to_be_visible()
        
    def filter_by_name(self,product_name):
        self.search_field.fill(product_name)
        self.search_field.press('Enter')
        self.show_product_result()
    
    def filter_by_price(self,price_range_min,price_range_max):
        self.min_price_range_field.fill(price_range_min)
        self.max_price_range_field.fill(price_range_max)
        self.max_price_range_field.press('Enter')
        self.show_product_result()
    
    def show_product_result(self):
        result_text = self.show_result.text_content()
        self.verify_product_exist(result_text)
        
    def verify_product_exist(self,text):
        count = re.search(r'\d+',text)
        result_count = int(count.group())
        if result_count > 0:
            expect(self.show_result).to_have_text(f'Showing {result_count} results   | ')
        else: 
            expect(self.error_product_not_found).to_be_visible()
            
        
    def verify_product_added_banner(self):
        expect(self.product_added_msg).to_be_visible()
        
    def verify_product_added_count(self,number_of_order):
        cart_btn = self.cart_btn.nth(0).text_content()
        cart_count = re.search(r'\d+',cart_btn)
        result_count = int(cart_count.group())
        if result_count == number_of_order:
            expect(self.cart_btn.nth(0)).to_contain_text(str(result_count))
        self.cart_btn.nth(0).click()
   
    def add_to_cart(self,entry_point,number_of_order):
        if entry_point == 'product_page':
            self.view_btn.click()
            self.product_add_to_cart_btn.click()
        elif entry_point == 'home_page':
            return self.number_of_orders(number_of_order)
    
    def number_of_orders(self,number_of_order):
        products = []
        if number_of_order > 1:
            for i in range(number_of_order):
                self.add_to_cart_btn.nth(i).click()
                products.append(
                    {
                        'name': self.product_name.nth(i).text_content().strip(),
                        'price': self.product_price.nth(i).text_content().replace('$','').strip()   
                    }
                )
        else:
            self.add_to_cart_btn.nth(0).click()
            products.append(
                {
                    'name': self.product_name.nth(0).text_content().strip(),
                    'price': self.product_price.nth(0).text_content().replace('$','').strip()
                }
            )
        return products