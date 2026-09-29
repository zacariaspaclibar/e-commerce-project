
from playwright.sync_api import expect
import pytest

from pages.Homepage import HomePage
from pages.cartPage import CartPage

@pytest.mark.parametrize('entry_point, number_of_order',[
    ('home_page', 1),
    ('home_page', 3)
])
def test_delete_product(authenticated_page,entry_point,number_of_order):
    home_page = HomePage(authenticated_page)
    home_page.add_to_cart(entry_point,number_of_order)
    cart_count = home_page.verify_product_added()
    if cart_count > 0:
        home_page.home_page_locators.cart_btn.nth(0).click()
    cart_page = CartPage(authenticated_page)
    cart_delete_btn = cart_page.cart_Page_Locator.delete_btn
    print(cart_delete_btn.count())
    # for i in range(cart_delete_btn.count()):
    #     cart_delete_btn.nth(i).click()
    # expect(cart_page.cart_Page_Locator.no_product_banner).to_be_visible()