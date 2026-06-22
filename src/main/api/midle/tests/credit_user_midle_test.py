import pytest
from src.main.api.midle.models.create_credit_request import CreditRequest
from src.main.api.midle.models.create_user_request import CreateUserRequest
from src.main.api.midle.requests.create_account_requester import CreateAccountRequester
from src.main.api.midle.requests.create_credit_requester import CreditRequester
from src.main.api.midle.requests.create_user_requester import CreateUserRequester
from src.main.api.midle.specs.request_specs import RequestSpecs
from src.main.api.midle.specs.response_specs import ResponseSpecs


@pytest.mark.midle_api
class TestCreateCreditAccount:
    def test_credit_user(self):
        create_user_request = CreateUserRequest(username="Kunershvili8", password="Pas!sw0rd", role="ROLE_CREDIT_SECRET")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili8", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        account_user_id = response.id

        create_credit_request = CreditRequest(accountId=account_user_id, amount=5000, termMonths=12)

        response_credit = CreditRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershvili8", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post(create_credit_request)

        assert response_credit.balance == 5000


    @pytest.mark.parametrize(
        "username, password, role, amount",
        [
            ("Kunershvili9", "Pas!sw0rd", "ROLE_CREDIT_SECRET", 4999),
            ("Kunershvili10", "Pas!sw0rd", "ROLE_CREDIT_SECRET",15001),
        ]
    )
    def test_invalid_credit(self, username, password, role, amount):
        create_user_request = CreateUserRequest(username=username, password=password, role=role)

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_created()
        ).post()

        account_user_id = response.id

        create_credit_request = CreditRequest(accountId=account_user_id, amount=amount, termMonths=12)

        CreditRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_bad()
        ).post(create_credit_request)


    def test_create_user(self):
        create_user_request = CreateUserRequest(username="Kunershvili11", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        create_user_request = CreateUserRequest(username="Kunershvili12", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

    @pytest.mark.parametrize(
        "username, password, amount",
        [
            ("Kunershvili11", "Pas!sw0rd", 4999),
            ("Kunershvili12", "Pas!sw0rd", 15001),
        ]
    )
    def test_invalid_role_credit(self, username, password, amount):

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_created()
        ).post()

        account_user_id = response.id

        create_credit_request = CreditRequest(accountId=account_user_id, amount=amount, termMonths=12)

        CreditRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            response_spec=ResponseSpecs.request_forbidden_403()
        ).post(create_credit_request)







