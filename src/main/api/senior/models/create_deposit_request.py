from typing import Annotated
from src.main.api.senior.models.base_model import BaseModel
from src.main.api.senior.generators.creation_rule import CreationRule


class CreateDepositRequest(BaseModel):
    accountId: Annotated[int, CreationRule(regex=r"^[1-9][0-9]{0,3}$")]
    amount: Annotated[float, CreationRule(regex=r"^(?:[1-8][0-9]{3}|9000)$")]