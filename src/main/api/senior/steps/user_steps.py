from src.main.api.senior.models.create_account_transfer_request import CreateTransferRequest
from src.main.api.senior.models.create_credit_repay_request import CreditRepayRequest
from src.main.api.senior.models.create_credit_request import CreditRequest
from src.main.api.senior.models.create_deposit_request import CreateDepositRequest
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.foundation.endpoint import Endpoint
from src.main.api.senior.foundation.requesters.crud_requester import CrudRequester
from src.main.api.senior.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.senior.specs.request_specs import RequestSpecs
from src.main.api.senior.specs.response_specs import ResponseSpecs
from src.main.api.senior.steps.base_steps import BaseSteps



class UserSteps(BaseSteps):

    """POSITIVE TESTS"""

    def create_account(self,create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def create_account_deposit(self, create_user_request: CreateUserRequest, create_deposit_request: CreateDepositRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT_DEPOSIT,
            ResponseSpecs.request_ok()
        ).post(create_deposit_request)
        return response

    def create_account_transfer(self, create_user_request: CreateUserRequest, create_deposit_request: CreateDepositRequest, create_transfer_request: CreateTransferRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT_TRANSFER,
            ResponseSpecs.request_ok()
        ).post(create_transfer_request)
        return response

    def create_user_credit(self, create_credit_user_request: CreateUserRequest, create_credit_request: CreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            Endpoint.CREATE_CREDIT,
            ResponseSpecs.request_created()
        ).post(create_credit_request)
        return response

    def create_user_repay_credit(self, create_credit_user_request: CreateUserRequest, create_repay_credit_request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            Endpoint.CREATE_REPAY_CREDIT,
            ResponseSpecs.request_ok()
        ).post(create_repay_credit_request)
        return response


    """NEGATIVE TESTS"""

    def create_invalid_accounts(self,create_user_request: CreateUserRequest):
        """не знаю как можно это оптимизировать сделав одним блоком"""
        ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post(create_user_request)

        ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post(create_user_request)

        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_conflict_409()
        ).post(create_user_request)

    def create_invalid_account_deposit(self, create_user_request: CreateUserRequest, create_deposit_request: CreateDepositRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT_DEPOSIT,
            ResponseSpecs.request_bad()
        ).post(create_deposit_request)

    def create_account_invalid_transfer(self, create_user_request: CreateUserRequest,create_deposit_request: CreateDepositRequest,create_account_transfer: CreateTransferRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT_TRANSFER,
            ResponseSpecs.request_bad()
        ).post(create_account_transfer)

    def create_invalid_user_credit(self, create_credit_user_request: CreateUserRequest, create_credit_request: CreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            Endpoint.CREATE_CREDIT,
            ResponseSpecs.request_bad()
        ).post(create_credit_request)

    def create_invalid_role_credit(self, create_user_request: CreateUserRequest, create_credit_request: CreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_CREDIT,
            ResponseSpecs.request_forbidden_403()
        ).post(create_credit_request)

    def create_user_invalid_repay_credit(self, create_credit_user_request: CreateUserRequest, create_repay_credit_request: CreditRepayRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            Endpoint.CREATE_REPAY_CREDIT,
            ResponseSpecs.request_unprocessable_entity_422()
        ).post(create_repay_credit_request)


