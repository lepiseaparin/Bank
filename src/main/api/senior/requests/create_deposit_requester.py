import requests
from http import HTTPStatus
from src.main.api.senior.models.create_deposit_request import CreateDepositRequest
from src.main.api.senior.models.create_deposit_response import CreateDepositResponse
from src.main.api.senior.requests.requester import Requester


class CreateDepositRequester(Requester):
    def post(self, create_deposit_request: CreateDepositRequest):
        url = f"{self.base_url}/account/deposit"
        response = requests.post(
            url = url,
            json = create_deposit_request.model_dump(),
            headers = self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreateDepositResponse(**response.json())
        return response
