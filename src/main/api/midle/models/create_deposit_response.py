from src.main.api.midle.models.base_model import BaseModel



class CreateDepositResponse(BaseModel):
    id: int
    balance: float