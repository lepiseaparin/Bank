import pytest
from sqlalchemy.orm import Session
from src.main.api.senior.classes.api_manager import ApiManager
from src.main.api.senior.db.crud.account_crud import AccountCrudDb as Account
from src.main.api.senior.fixtures.db_fixture import db_session
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.models.login_user_request import LoginUserRequest


@pytest.mark.senior_api
class TestCreateAccount:
    def test_create_account(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest):
        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0

        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.id == response.id, "Ошибка. Аккаунт не создан, id аккаунта нет в БД"
        assert account_from_db.balance == response.balance, "Ошибка. Поле баланса отсутствует в БД"


    def test_invalid_create_account(self, db_session: Session, api_manager: ApiManager, login_admin_request: LoginUserRequest, create_user_request: CreateUserRequest):
        response_admin = api_manager.admin_steps.create_invalide_admin_account(login_admin_request)
        admin_account_from_db = Account.get_account_by_id(db_session, response_admin) # не думаю, что так правильно

        assert admin_account_from_db is None, "Ошибка. Аккаунт создан"

        response_user = api_manager.user_steps.create_invalid_accounts(create_user_request)
        user_account_from_db = Account.get_account_by_id(db_session, response_user)

        assert user_account_from_db is None, "Ошибка. Аккаунт создан" # не думаю, что так правильно.