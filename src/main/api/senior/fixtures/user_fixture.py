import pytest
from src.main.api.senior.models.create_account_transfer_request import CreateTransferRequest
from src.main.api.senior.models.create_credit_request import CreditRequest
from src.main.api.senior.generators.model_generator import RandomModelGenerator
from src.main.api.senior.models.create_credit_repay_request import CreditRepayRequest
from src.main.api.senior.models.create_deposit_request import CreateDepositRequest
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.models.login_user_request import LoginUserRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_credit_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    user_request.role = "ROLE_CREDIT_SECRET"
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def login_admin_request(api_manager):
    user_request = LoginUserRequest(username="admin", password="123456")
    api_manager.admin_steps.login_user(user_request)
    return user_request

@pytest.fixture
def create_deposit_request(api_manager, create_user_request):
    account = api_manager.user_steps.create_account(create_user_request)
    create_deposit_request = RandomModelGenerator.generate(CreateDepositRequest)
    create_deposit_request.accountId = account.id

    return create_deposit_request

@pytest.fixture
def create_transfer_request(api_manager, create_user_request, create_deposit_request):
    from_user_request = api_manager.user_steps.create_account_deposit(create_user_request, create_deposit_request)
    to_user_request = api_manager.user_steps.create_account(create_user_request)
    account_transfer = RandomModelGenerator.generate(CreateTransferRequest)
    account_transfer.fromAccountId = from_user_request.id
    account_transfer.toAccountId = to_user_request.id

    return account_transfer

@pytest.fixture
def create_credit_request(api_manager, create_credit_user_request):
    user_request = api_manager.user_steps.create_account(create_credit_user_request)
    create_credit = RandomModelGenerator.generate(CreditRequest)
    create_credit.accountId = user_request.id
    return create_credit

@pytest.fixture
def create_repay_credit_request(api_manager, create_credit_user_request, create_credit_request):
    account_id, amount = create_credit_request.accountId, create_credit_request.amount
    respone_credit = api_manager.user_steps.create_user_credit(create_credit_user_request, create_credit_request)
    credit_id = respone_credit.creditId
    credit_repay = CreditRepayRequest(creditId=credit_id,accountId= account_id,amount= amount)
    return credit_repay






