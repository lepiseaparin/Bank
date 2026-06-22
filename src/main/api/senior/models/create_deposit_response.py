from src.main.api.senior.models.base_model import BaseModel



class CreateDepositResponse(BaseModel):
    id: int
    balance: float