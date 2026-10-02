
from playwright.sync_api import expect
import pytest

from pages.Homepage import HomePage
from pages.cartPage import CartPage
from pages.checkoutPage import CheckoutPage
from pages.orderDetailsPage import OrderDetailsPage

@pytest.mark.parametrize('entry_point, number_of_order',[
    ('home_page', 1)
])
def test_delete_product(authenticated_page,entry_point,number_of_order):
    home_page = HomePage(authenticated_page)
    home_page.add_to_cart(entry_point,number_of_order)
    home_page.verify_product_added_count(number_of_order)
    cart_page = CartPage(authenticated_page)
    cart_page.verify_delete_cart_items()

@pytest.mark.parametrize('entry_point, number_of_order',[
    ('home_page', 3)
])
def test_checkout_order(authenticated_page,entry_point,number_of_order):
    home_page = HomePage(authenticated_page)
    products = home_page.add_to_cart(entry_point,number_of_order)
    home_page.verify_product_added_count(number_of_order)
    cart_page = CartPage(authenticated_page)
    checkout_products = cart_page.product_checkout(products)
    checkout_page = CheckoutPage(authenticated_page)
    # list_order = checkout_page.checkout_page_locators.checkout_product_name
    # product_id = []
    # for i in range(list_order.count()):
    #     if checkout_products[i]['name'] == checkout_page.checkout_page_locators.checkout_product_name.nth(i).text_content().strip():
    #         product_id.append(checkout_products[i]['id'])
    # print(product_id)
    checkout_page.checkout_page_locators.country_field.click()
    checkout_page.checkout_page_locators.country_field.press_sequentially('Phil')
    expect(checkout_page.checkout_page_locators.country_name_btn).to_be_visible()
    checkout_page.checkout_page_locators.country_name_btn.click()
    checkout_page.checkout_page_locators.place_order_btn.click()
    order_details_page = OrderDetailsPage(authenticated_page)
    for i in range(order_details_page.order_details_locators.order_id.count()):
        if checkout_products[i]['id'] == order_details_page.order_details_locators.order_id.nth(i).text_content().replace('|','').strip():
            expect(order_details_page.order_details_locators.order_id.nth(i).text_content()).to_be_visible()
            
        print(f"checkout id: {checkout_products[i]['id']}")
        print(f"Order id: {order_details_page.order_details_locators.order_id.nth(i).text_content().replace('|','').strip()}")
    
        