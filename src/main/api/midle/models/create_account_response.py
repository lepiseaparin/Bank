from src.main.api.midle.models.base_model import BaseModel


class CreateAccountResponse(BaseModel):
    id: int
    number: str
    balance: float