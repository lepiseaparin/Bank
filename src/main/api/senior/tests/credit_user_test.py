import pytest
from sqlalchemy.orm import Session
from src.main.api.senior.classes.api_manager import ApiManager
from src.main.api.senior.fixtures.api_fixture import api_manager
from src.main.api.senior.models.create_credit_request import CreditRequest
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.db.crud.credit_crud import CreditCrudDb as Credit


@pytest.mark.senior_api
class TestCreateCredit:
    def test_credit_user(self, db_session: Session, api_manager: ApiManager, create_credit_user_request: CreateUserRequest, create_credit_request: CreditRequest):
        response = api_manager.user_steps.create_user_credit(create_credit_user_request, create_credit_request)

        assert response.balance == create_credit_request.amount

        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)

        assert credit_from_db.id == response.creditId, "Ошибка. Id кредита не найден"
        assert credit_from_db.balance == - response.balance, "Ошибка. Баланс кредита не найден"


    @pytest.mark.parametrize(
        "amount",
        [
            (4999),
            (15001),
        ]
    )
    def test_invalid_credit(self, db_session: Session, api_manager: ApiManager, create_credit_user_request: CreateUserRequest, create_credit_request: CreditRequest, amount: float):
        create_credit_request.amount = amount
        api_manager.user_steps.create_invalid_user_credit(create_credit_user_request, create_credit_request)


    def test_invalid_role_credit(self, api_manager, create_user_request, create_credit_request):
        api_manager.user_steps.create_invalid_role_credit(create_user_request, create_credit_request)







