import pytest
from sqlalchemy.orm import Session
from src.main.api.senior.classes.api_manager import ApiManager
from src.main.api.senior.fixtures.user_fixture import create_repay_credit_request
from src.main.api.senior.models.create_credit_request import CreditRequest
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.db.crud.credit_crud import CreditCrudDb as Credit


@pytest.mark.senior_api
class TestRepayCreditUser:
    def test_credit_repay(self, db_session: Session, api_manager: ApiManager, create_credit_user_request: CreateUserRequest, create_repay_credit_request: CreditRequest):
        response = api_manager.user_steps.create_user_repay_credit(create_credit_user_request, create_repay_credit_request)

        assert response.amountDeposited == create_repay_credit_request.amount

        from_repay_credit_db = Credit.get_credit_by_id(db_session, response.creditId)

        assert from_repay_credit_db.id == response.creditId, "Ошибка. CreditId не найден"
        assert from_repay_credit_db.amount == response.amountDeposited, "Ошибка. Баланс кредита не совпадает с суммой"



    @pytest.mark.parametrize(
        "amount",
        [
            (4999),
            (15001),
        ]
    )
    def test_invalid_repay_credit(self, api_manager: ApiManager, create_credit_user_request: CreateUserRequest, create_repay_credit_request: CreditRequest, amount):
        create_repay_credit_request.amount = amount
        api_manager.user_steps.create_user_invalid_repay_credit(create_credit_user_request, create_repay_credit_request)






