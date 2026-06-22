from src.main.api.senior.foundation.endpoint import Endpoint
from src.main.api.senior.foundation.requesters.crud_requester import CrudRequester
from src.main.api.senior.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.models.login_user_request import LoginUserRequest
from src.main.api.senior.specs.request_specs import RequestSpecs
from src.main.api.senior.specs.response_specs import ResponseSpecs
from src.main.api.senior.steps.base_steps import BaseSteps


class AdminSteps(BaseSteps):
    def create_user(self,create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.request_ok()
        ).post(create_user_request)

        self.created_obj.append(response)
        return response


    def delete_user(self,user_id: int):
        CrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_DELETE_USER,
            ResponseSpecs.request_ok()
        ).delete(user_id)


    def create_invalid_user(self,create_user_request: CreateUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.request_bad()
        ).post(create_user_request)


    def login_user(self,login_user_request: LoginUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.unauth_headers(),
            Endpoint.LOGIN_USER,
            ResponseSpecs.request_ok()
        ).post(login_user_request)
        return response

    def create_invalide_admin_account(self, login_admin_request: LoginUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_forbidden_403()
        ).post(login_admin_request)


