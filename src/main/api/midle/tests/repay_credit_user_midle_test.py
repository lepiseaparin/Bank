import pytest
from src.main.api.midle.models.create_credit_repay_request import CreditRepayRequest
from src.main.api.midle.models.create_credit_request import CreditRequest
from src.main.api.midle.models.create_user_request import CreateUserRequest
from src.main.api.midle.requests.create_account_requester import CreateAccountRequester
from src.main.api.midle.requests.create_credit_repay_requester import CreditRepayRequester
from src.main.api.midle.requests.create_credit_requester import CreditRequester
from src.main.api.midle.requests.create_user_requester import CreateUserRequester
from src.main.api.midle.specs.request_specs import RequestSpecs
from src.main.api.midle.specs.response_specs import ResponseSpecs


@pytest.mark.midle_api
class TestRepayCreditUser:
    def test_credit_repay(self):
        create_user_request = CreateUserRequest(username="Kunershvili13", password="Pas!sw0rd", role="ROLE_CREDIT_SECRET")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili13", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        account_user_id = response.id

        create_credit_request = CreditRequest(accountId=account_user_id, amount=5000, termMonths=12)

        response_credit = CreditRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili13", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post(create_credit_request)

        credit_id = response_credit.creditId

        create_credit_repay_request = CreditRepayRequest(creditId=credit_id,accountId=account_user_id,amount=5000)
        response_repay_credit = CreditRepayRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili13", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_credit_repay_request)

        assert response_repay_credit.amountDeposited == 5000


    def test_create_user(self):
        create_user_request = CreateUserRequest(username="Kunershvili14", password="Pas!sw0rd", role="ROLE_CREDIT_SECRET")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        create_user_request = CreateUserRequest(username="Kunershvili15", password="Pas!sw0rd", role="ROLE_CREDIT_SECRET")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)


    @pytest.mark.parametrize(
        "username, password, amount",
        [
            ("Kunershvili14", "Pas!sw0rd", 4999),
            ("Kunershvili15", "Pas!sw0rd", 15001),
        ]
    )
    def test_invalid_repay_credit(self, username, password, amount):

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_created()
        ).post()

        account_user_id = response.id

        create_credit_request = CreditRequest(accountId=account_user_id, amount=5000, termMonths=12)

        response_credit = CreditRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_created()
        ).post(create_credit_request)

        credit_id = response_credit.creditId

        create_credit_repay_request = CreditRepayRequest(creditId=credit_id,accountId=account_user_id,amount=amount)
        CreditRepayRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_unprocessable_entity_422()
        ).post(create_credit_repay_request)





