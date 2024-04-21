from pydantic import BaseModel, EmailStr, PositiveInt, Field


class User(BaseModel):
    id: PositiveInt
    age: int = Field(default=1, gt=0, lt=120)
    first_name: str = "User"
    second_name: str = "Userskiy"
    username: str = "username"
    email: EmailStr = "user@example.com"
