from src.main.api.midle.models.base_model import BaseModel



class CreateDepositRequest(BaseModel):
    accountId: int
    amount: float