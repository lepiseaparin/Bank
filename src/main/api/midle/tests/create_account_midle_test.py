import pytest
from src.main.api.midle.models.create_user_request import CreateUserRequest
from src.main.api.midle.requests.create_account_requester import CreateAccountRequester
from src.main.api.midle.requests.create_user_requester import CreateUserRequester
from src.main.api.midle.specs.request_specs import RequestSpecs
from src.main.api.midle.specs.response_specs import ResponseSpecs


@pytest.mark.midle_api
class TestCreateAccount:
    def test_login_admin(self):
        create_user_request = CreateUserRequest(username="Kuneridze7", password="Pas!sw0rd", role="ROLE_USER")

        response = CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kuneridze7", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        assert response.balance == 0



    def test_invalid_create_account(self):
        CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_forbidden_403()
        ).post()

        create_user_request = CreateUserRequest(username="Kunershili1", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershili1", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershili1", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Kunershili1", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_conflict_409()
        ).post()







