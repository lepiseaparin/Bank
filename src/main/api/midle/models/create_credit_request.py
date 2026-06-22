from src.main.api.midle.models.base_model import BaseModel



class CreditRequest(BaseModel):
    accountId: int
    amount: float
    termMonths: int