import pytest
from sqlalchemy.orm import Session

from src.main.api.senior.classes.api_manager import ApiManager
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.generators.model_generator import RandomModelGenerator
from src.main.api.senior.db.crud.user_crud import UserCrudDb as User


@pytest.mark.senior_api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_user(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, "Ошибка. Созданного пользователя нет в БД, ошибка"


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
    def test_create_user_invalid(self, db_session: Session, username: str, password: str, api_manager: ApiManager):

        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db is None, "Ошибка. Пользователь создан"

