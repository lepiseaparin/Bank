from src.main.api.midle.models.base_model import BaseModel


class CreditRepayRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float