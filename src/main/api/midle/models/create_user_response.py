from src.main.api.midle.models.base_model import BaseModel

class CreateUserResponse(BaseModel):
    id: int
    username: str
    password: str
    role: str