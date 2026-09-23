import pytest
from pages.Homepage import HomePage

def test_green_banner(authenticated_page):
    home_page = HomePage(authenticated_page)
    home_page.verify_green_banner()
    
@pytest.mark.parametrize(
    'product_name',[
        'ADIDAS',
        'ZARA',
        'iphone',
        'adidas'
    ])
def test_filter_by_name(authenticated_page,product_name):
    home_page = HomePage(authenticated_page)
    home_page.filter_by_name(product_name)

@pytest.mark.parametrize('price_range_min, price_range_max',[
    ('11000','11499'),
    ('11000','11500'),
    ('11500','55000'),
    ('30000','55000'),
    ('55001','60000')
])
def test_filter_by_price(authenticated_page,price_range_min,price_range_max):
    home_page = HomePage(authenticated_page)
    home_page.filter_by_price(price_range_min,price_range_max)
