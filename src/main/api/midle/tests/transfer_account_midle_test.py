import pytest
import requests

from src.main.api.midle.models.create_account_transfer_request import CreateTransferRequest
from src.main.api.midle.models.create_deposit_request import CreateDepositRequest
from src.main.api.midle.models.create_user_request import CreateUserRequest
from src.main.api.midle.requests.create_account_requester import CreateAccountRequester
from src.main.api.midle.requests.create_account_transfer_requester import CreateTransferRequester
from src.main.api.midle.requests.create_deposit_requester import CreateDepositRequester
from src.main.api.midle.requests.create_user_requester import CreateUserRequester
from src.main.api.midle.specs.request_specs import RequestSpecs
from src.main.api.midle.specs.response_specs import ResponseSpecs

@pytest.mark.midle_api
class TestTransferAccount:
    def test_login_admin(self):
        create_user_request_user1 = CreateUserRequest(username="Kunershvili2", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request_user1)

        response_user1 = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili2", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        from_account_id = response_user1.id

        create_deposit_request = CreateDepositRequest(accountId=from_account_id ,amount=1500)

        response_deposit = CreateDepositRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili2", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_ok()

        ).post(create_deposit_request)

        assert response_deposit.balance == 1500

        create_user_request_user2 = CreateUserRequest(username="Kunershvili3", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request_user2)

        response_user2 = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili3", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        to_account_id = response_user2.id

        create_transfer_request = CreateTransferRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=1000)

        response_transfer = CreateTransferRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili2", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_transfer_request)

        assert response_transfer.fromAccountIdBalance == 500


    @pytest.mark.parametrize(
        "user1_login, user2_login, password_user1, password_user2, transfer",
        [
            ("Kunershvili4", "Kunershvili5", "Pas!sw0rd", "Pas!sw0rd", 499),
            ("Kunershvili6", "Kunershvili7", "Pas!sw0rd", "Pas!sw0rd", 10001)
        ]
    )
    def test_invalid_transfer(self, user1_login, user2_login, password_user1, password_user2, transfer):
        create_user_request_user1 = CreateUserRequest(username=user1_login, password=password_user1, role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request_user1)

        response_user1 = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username=user1_login, password=password_user1),
            response_spec=ResponseSpecs.request_created()
        ).post()

        from_account_id = response_user1.id

        create_deposit_request = CreateDepositRequest(accountId=from_account_id ,amount=1000)

        response_deposit = CreateDepositRequester(
            request_spec=RequestSpecs.auth_headers(username=user1_login, password=password_user1),
            response_spec=ResponseSpecs.request_ok()

        ).post(create_deposit_request)

        assert response_deposit.balance == 1000

        create_user_request_user2 = CreateUserRequest(username=user2_login, password=password_user2, role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request_user2)

        response_user2 = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username=user2_login, password=password_user2),
            response_spec=ResponseSpecs.request_created()
        ).post()

        to_account_id = response_user2.id

        create_transfer_request = CreateTransferRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=transfer)

        CreateTransferRequester(
            request_spec=RequestSpecs.auth_headers(username=user1_login, password=password_user1),
            response_spec=ResponseSpecs.request_bad()
        ).post(create_transfer_request)

