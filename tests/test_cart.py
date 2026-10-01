
import pytest

from pages.Homepage import HomePage
from pages.cartPage import CartPage

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
    cart_page.product_checkout(products)
        