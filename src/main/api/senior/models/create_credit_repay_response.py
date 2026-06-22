from src.main.api.senior.models.base_model import BaseModel


class CreditRepayResponse(BaseModel):
    creditId: int
    amountDeposited: float