from src.main.api.midle.models.base_model import BaseModel

class LoginUserRequest(BaseModel):
    username: str
    password: str
