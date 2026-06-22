from src.main.api.midle.models.base_model import BaseModel


class CreateTransferRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: float