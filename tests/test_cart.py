
from playwright.sync_api import expect
import pytest

from pages.Homepage import HomePage
from pages.cartPage import CartPage

@pytest.mark.parametrize('entry_point',['home_page'])
def test_delete_product(authenticated_page,entry_point):
    home_page = HomePage(authenticated_page)
    home_page.add_to_cart(entry_point)
    cart_count = home_page.verify_product_added()
    if cart_count == 1:
        home_page.home_page_locators.cart_btn.nth(0).click()
    cart_page = CartPage(authenticated_page)
    cart_page.cart_Page_Locator.delete_btn.click()
    expect(cart_page.cart_Page_Locator.no_product_banner).to_be_visible()