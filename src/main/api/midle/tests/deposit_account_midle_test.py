import pytest
from src.main.api.midle.models.create_deposit_request import CreateDepositRequest
from src.main.api.midle.models.create_user_request import CreateUserRequest
from src.main.api.midle.requests.create_account_requester import CreateAccountRequester
from src.main.api.midle.requests.create_deposit_requester import CreateDepositRequester
from src.main.api.midle.requests.create_user_requester import CreateUserRequester
from src.main.api.midle.specs.request_specs import RequestSpecs
from src.main.api.midle.specs.response_specs import ResponseSpecs


@pytest.mark.midle_api
class TestDepositAccount:
    def test_create_deposit(self):
        create_user_request = CreateUserRequest(username="Kuneringo3", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kuneringo3", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        account_id = response.id

        create_deposit_request = CreateDepositRequest(accountId=account_id ,amount=1000)

        response_deposit = CreateDepositRequester(
            request_spec=RequestSpecs.auth_headers(username="Kuneringo3", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_ok()

        ).post(create_deposit_request)

        assert response_deposit.balance == 1000


    @pytest.mark.parametrize(
        "username, password, deposit",
        [
            ("Kuneringo4","Pas!sw0rd",999),
            ("Kuneringo20","Pas!sw0rd",9001)
        ]
    )
    def test_invalid_deposit(self, username,password,deposit):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_created()
        ).post()

        account_id = response.id

        create_deposit_request = CreateDepositRequest(accountId=account_id, amount=deposit)

        CreateDepositRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_bad()

        ).post(create_deposit_request)








