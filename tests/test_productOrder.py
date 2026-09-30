import pytest
from pages.Homepage import HomePage

@pytest.mark.parametrize('entry_point, number_of_order',[
    ('product_page', 1),
    ('home_page', 1),
    ('home_page', 3)
])
def test_add_to_cart(authenticated_page,entry_point,number_of_order):
    home_page = HomePage(authenticated_page)
    home_page.add_to_cart(entry_point,number_of_order)
    home_page.verify_product_added(number_of_order)
    home_page.verify_product_added_banner()

