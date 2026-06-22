from src.main.api.senior.models.base_model import BaseModel


class CreateAccountResponse(BaseModel):
    id: int
    number: str
    balance: float