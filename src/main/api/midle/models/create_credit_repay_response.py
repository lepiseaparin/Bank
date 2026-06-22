from src.main.api.midle.models.base_model import BaseModel


class CreditRepayResponse(BaseModel):
    creditId: int
    amountDeposited: float