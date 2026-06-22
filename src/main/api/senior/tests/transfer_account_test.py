import pytest
from sqlalchemy.orm import Session
from src.main.api.senior.classes.api_manager import ApiManager
from src.main.api.senior.models.create_account_transfer_request import CreateTransferRequest
from src.main.api.senior.models.create_deposit_request import CreateDepositRequest
from src.main.api.senior.models.create_user_request import CreateUserRequest
from src.main.api.senior.db.crud.transaction_crud import TransactionCrudDb as Transaction

@pytest.mark.senior_api
class TestCreateTransfer:
    def test_create_transfer_account(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest, create_deposit_request: CreateDepositRequest, create_transfer_request: CreateTransferRequest) -> None:
        response = api_manager.user_steps.create_account_transfer(create_user_request, create_deposit_request, create_transfer_request)

        assert response.fromAccountIdBalance ==  create_deposit_request.amount - create_transfer_request.amount

        transfer_from_db = Transaction.get_transaction_by_ids(db_session, create_transfer_request.toAccountId, create_transfer_request.fromAccountId)

        assert transfer_from_db.to_account_id == response.toAccountId, "Ошибка, не найден id аккаунта"
        assert transfer_from_db.from_account_id == response.fromAccountId, "Ошибка, не найден id аккаунта"
        assert transfer_from_db.amount == create_transfer_request.amount, "Ошибка, не найдено поле amount"


    @pytest.mark.parametrize(
        "transfer",
        [
            (499),
            (10001)
        ]
    )
    def test_invalid_transfer(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest, create_deposit_request: CreateDepositRequest, create_transfer_request: CreateTransferRequest, transfer: float):
        create_transfer_request.amount = transfer
        api_manager.user_steps.create_account_invalid_transfer(create_user_request, create_deposit_request, create_transfer_request)



