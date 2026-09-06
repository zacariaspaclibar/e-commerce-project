class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client',wait_until="domcontentloaded",
    timeout=60000
)