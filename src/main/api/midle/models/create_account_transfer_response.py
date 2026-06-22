from src.main.api.midle.models.base_model import BaseModel


class CreateTransferResponse(BaseModel):
    fromAccountId: int
    toAccountId: int
    fromAccountIdBalance: float