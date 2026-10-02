
from playwright.sync_api import expect
import pytest

from pages.Homepage import HomePage
from pages.cartPage import CartPage
from pages.checkoutPage import CheckoutPage
from pages.orderDetailsPage import OrderDetailsPage
from data import test_data

@pytest.mark.parametrize('entry_point, number_of_order',[
    test_data.DEFAULT_SINGLE_ORDER
])
def test_delete_product(authenticated_page,entry_point,number_of_order):
    home_page = HomePage(authenticated_page)
    home_page.add_to_cart(entry_point,number_of_order)
    home_page.verify_product_added_count(number_of_order)
    cart_page = CartPage(authenticated_page)
    cart_page.verify_delete_cart_items()

@pytest.mark.parametrize('entry_point, number_of_order, country',[
    test_data.DEFAULT_SINGLE_ORDER_WITH_COUNRTY
])
def test_checkout_order(authenticated_page,entry_point,number_of_order,country):
    home_page = HomePage(authenticated_page)
    products = home_page.add_to_cart(entry_point,number_of_order)
    home_page.verify_product_added_count(number_of_order)
    cart_page = CartPage(authenticated_page)
    checkout_products = cart_page.product_checkout(products)
    checkout_page = CheckoutPage(authenticated_page)
    checkout_page.fill_shipping_info(country)
    order_details_page = OrderDetailsPage(authenticated_page)
    order_details_page.verify_order_in_cart_match(checkout_products)