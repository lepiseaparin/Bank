import requests
from http import HTTPStatus

from src.main.api.senior.models.create_account_transfer_request import CreateTransferRequest
from src.main.api.senior.models.create_account_transfer_response import CreateTransferResponse
from src.main.api.senior.requests.requester import Requester


class CreateTransferRequester(Requester):
    def post(self, create_transfer_request: CreateTransferRequest):
        url = f"{self.base_url}/account/transfer"
        response = requests.post(
            url=url,
            json=create_transfer_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreateTransferResponse(**response.json())
        return response
