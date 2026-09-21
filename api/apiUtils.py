from playwright.sync_api import Playwright
from data import credentials

class APIUTILS:
   
    def api_token(self,username,password,playwright):
        api_request_context = playwright.request.new_context(base_url=credentials.BASED_URL)
        response = api_request_context.post(url='/api/ecom/auth/login',data={
            'userEmail': username,
            'userPassword': password
        })
        assert response.ok
        responseBody = response.json()
        return responseBody['token']