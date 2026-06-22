from src.main.api.senior.models.create_account_response import CreateAccountResponse
from src.main.api.senior.models.create_credit_repay_response import CreditRepayResponse
from src.main.api.senior.models.create_deposit_response import CreateDepositResponse
from src.main.api.senior.models.base_model import BaseModel
from typing import Optional, Type
from dataclasses import dataclass
from enum import Enum
from src.main.api.senior.models.create_account_transfer_request import CreateTransferRequest
from src.main.api.senior.models.create_account_transfer_response import CreateTransferResponse
from src.main.api.senior.models.create_credit_request import CreditRequest
from src.main.api.senior.models.create_credit_response import CreditResponse
from src.main.api.senior.models.create_deposit_request import CreateDepositRequest
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.models.create_user_response import CreateUserResponse
from src.main.api.senior.models.login_user_request import LoginUserRequest
from src.main.api.senior.models.login_user_response import LoginUserResponse


@dataclass
class EndpointConfigConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class  Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfigConfiguration(
        request_model=CreateUserRequest,
        url="/admin/create",
        response_model=CreateUserResponse
    )

    ADMIN_DELETE_USER = EndpointConfigConfiguration(
        request_model=None,
        url="/admin/users",
        response_model=None
    )

    LOGIN_USER = EndpointConfigConfiguration(
        request_model=LoginUserRequest,
        url="/auth/token/login",
        response_model=LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfigConfiguration(
        request_model=None,
        url="/account/create",
        response_model=CreateAccountResponse
    )

    CREATE_ACCOUNT_DEPOSIT = EndpointConfigConfiguration(
        request_model=CreateDepositRequest,
        url="/account/deposit",
        response_model=CreateDepositResponse
    )

    CREATE_ACCOUNT_TRANSFER = EndpointConfigConfiguration(
        request_model=CreateTransferRequest,
        url="/account/transfer",
        response_model=CreateTransferResponse
    )

    CREATE_CREDIT = EndpointConfigConfiguration(
        request_model=CreditRequest,
        url="/credit/request",
        response_model=CreditResponse
    )

    CREATE_REPAY_CREDIT = EndpointConfigConfiguration(
        request_model=CreditRequest,
        url="/credit/repay",
        response_model=CreditRepayResponse
    )