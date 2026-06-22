from src.main.api.senior.models.base_model import BaseModel


class CreditRepayRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float