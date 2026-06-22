import pytest
from src.main.api.midle.models.login_user_request import LoginUserRequest
from src.main.api.midle.models.create_user_request import CreateUserRequest
from src.main.api.midle.requests.create_user_requester import CreateUserRequester
from src.main.api.midle.requests.login_user_requester import LoginUserRequester
from src.main.api.midle.specs.request_specs import RequestSpecs
from src.main.api.midle.specs.response_specs import ResponseSpecs


@pytest.mark.midle_api
class TestUserLogin:
    def test_login_admin(self):
        login_user_request = LoginUserRequest(username="admin", password="123456")

        response =  LoginUserRequester(
            request_spec=RequestSpecs.unauth_headers(),
            response_spec=ResponseSpecs.request_ok()
        ).post(login_user_request)


        assert login_user_request.username == response.user.username
        assert response.user.role == "ROLE_ADMIN"

    def test_login_user(self):
        create_user_request = CreateUserRequest(username="Kuneridze6", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        login_user_request = LoginUserRequest(username="Kuneridze6", password="Pas!sw0rd")

        response =  LoginUserRequester(
            request_spec=RequestSpecs.unauth_headers(),
            response_spec=ResponseSpecs.request_ok()
        ).post(login_user_request)


        assert login_user_request.username == response.user.username
        assert response.user.role == "ROLE_USER"