from typing import Annotated
from src.main.api.senior.models.base_model import BaseModel
from src.main.api.senior.generators.creation_rule import CreationRule


class CreateTransferRequest(BaseModel):
    fromAccountId: Annotated[int, CreationRule(regex=r"^[1-9][0-9]{0,3}$")]
    toAccountId: Annotated[int, CreationRule(regex=r"^[1-9][0-9]{0,3}$")]
    amount: Annotated[float, CreationRule(regex=r"^(?:[5-9][0-9]{2}|1000)$")]