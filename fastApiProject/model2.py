from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, Field, constr, PositiveInt

# Создаем перечисление для поля sex
class Gender(str, Enum):
    male = "male"
    female = "female"

# Создаем класс Actor с провалидированными полями, используя Pydantic
class Actor(BaseModel):
    actor_id: PositiveInt
    name: constr(min_length=2, max_length=20)
    surname: constr(min_length=2, max_length=20)
    age: int = Field(..., ge=0, le=100)
    sex: Gender

# Создаем объект класса FastAPI
app = FastAPI()

# Создаем эндпоинт с POST запросом для приема данных об актере и их возврата
@app.post("/create_actor/")
async def create_actor(actor: Actor):
    return actor