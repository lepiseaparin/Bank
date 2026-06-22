import pytest
from sqlalchemy.orm import Session
from src.main.api.senior.classes.api_manager import ApiManager
from src.main.api.senior.fixtures.api_fixture import api_manager
from src.main.api.senior.models.create_deposit_request import CreateDepositRequest
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.db.crud.account_crud import AccountCrudDb as Account


@pytest.mark.senior_api
class TestDepositAccount:
    def test_create_deposit(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest, create_deposit_request: CreateDepositRequest):
        response = api_manager.user_steps.create_account_deposit(create_user_request, create_deposit_request)

        assert response.balance == create_deposit_request.amount

        from_deposit_db = Account.get_account_by_id(db_session, response.id)

        assert from_deposit_db.balance == create_deposit_request.amount


    @pytest.mark.parametrize(
        "amount",
        [
            (999),
            (9001)
        ]
    )
    def test_invalid_deposit(self,db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest, create_deposit_request: CreateDepositRequest, amount):
        create_deposit_request.amount = amount
        api_manager.user_steps.create_invalid_account_deposit(create_user_request, create_deposit_request)

