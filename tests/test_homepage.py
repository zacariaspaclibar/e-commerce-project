from pages.Homepage import HomePage

def test_green_banner(authenticated_page):
    home_page = HomePage(authenticated_page)
    home_page.verify_green_banner()
    
