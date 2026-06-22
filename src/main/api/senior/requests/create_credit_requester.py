from http import HTTPStatus
import requests
from src.main.api.senior.models.create_credit_request import CreditRequest
from src.main.api.senior.models.create_credit_response import CreditResponse
from src.main.api.senior.requests.requester import Requester




class CreditRequester(Requester):
    def post(self, create_credit_request: CreditRequest):
        url = f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json=create_credit_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreditResponse(**response.json())
        return response
