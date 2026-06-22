import pytest
from src.main.api.midle.models.create_user_request import CreateUserRequest
from src.main.api.midle.requests.create_user_requester import CreateUserRequester
from src.main.api.midle.specs.request_specs import RequestSpecs
from src.main.api.midle.specs.response_specs import ResponseSpecs


@pytest.mark.midle_api
class TestCreateUser:
    def test_create_user(self):
        create_user_request = CreateUserRequest(username="Kuneridze5", password="Pas!sw0rd", role="ROLE_USER")

        response = CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role



    @pytest.mark.parametrize(
        "username, password",
        [
            ("хуй", "Pas!sw0rd" ),
            ("ab", "Pas!sw0rd"),
            ("abc!", "Pas!sw0rd"),
            ("Kuner14", "Pas!sw0rд"),
            ("Kuner15", "Passw!9"),
            ("Kuner16", "passw!o9d"),
            ("Kuner17", "PASSWO!O9D"),
            ("Kuner18", "PASSWo9Dd"),
            ("Kuner19", "PASSWWo!Dd"),
        ]
    )
    def test_create_user_invalid(self, username, password):

        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_bad()
        ).post(create_user_request)

