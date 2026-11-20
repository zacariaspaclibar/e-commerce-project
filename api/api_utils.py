from playwright.sync_api import Playwright

from config.settings import API_BASE_URL


class ApiUtils:
   
    def api_token(self,username,password,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url=API_BASE_URL)
        response = api_request_context.post(url='/api/ecom/auth/login',data={
            'userEmail': username,
            'userPassword': password
        })
        assert response.ok
        responseBody = response.json()
        return responseBody['token']
    
    def order_id(self,auth_token, playwright:Playwright,country,product_order_id):
        api_request_context = playwright.request.new_context(base_url = API_BASE_URL)
        response = api_request_context.post(
            url='/api/ecom/order/create-order',
            data={
            "orders":[
                {
                    "country":country,
                    "productOrderedId":product_order_id
                    }
                ]
            },
            headers={
                'Content-Type':'application/json',
                'Authorization': auth_token
            }
        )
        response_body = response.json()
        order_id = response_body['orders'][0]
        return order_id