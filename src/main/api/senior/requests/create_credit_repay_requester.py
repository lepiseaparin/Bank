import requests
from http import HTTPStatus
from src.main.api.senior.models.create_credit_repay_request import CreditRepayRequest
from src.main.api.senior.models.create_credit_repay_response import CreditRepayResponse
from src.main.api.senior.requests.requester import Requester


class CreditRepayRequester(Requester):
    def post(self,create_credit_repay_request: CreditRepayRequest):
        url = f"{self.base_url}/credit/repay"
        response = requests.post(
            url = url,
            json = create_credit_repay_request.model_dump(),
            headers = self.headers,
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreditRepayResponse(**response.json())
        return response