import pytest
from pages.Homepage import HomePage
from data import test_data

@pytest.mark.parametrize('entry_point, number_of_order',[
    test_data.ALTERNATIVE_SINGLE_ORDER,
    test_data.DEFAULT_SINGLE_ORDER,
    test_data.DEFAULT_MULTI_ORDER
])
def test_add_to_cart(authenticated_page,entry_point,number_of_order):
    home_page = HomePage(authenticated_page)
    home_page.add_to_cart(entry_point,number_of_order)
    home_page.verify_product_added_banner()
    home_page.verify_product_added_count(number_of_order)

