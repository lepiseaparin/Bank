from src.main.api.senior.models.base_model import BaseModel

class CreateUserResponse(BaseModel):
    id: int
    username: str
    password: str
    role: str