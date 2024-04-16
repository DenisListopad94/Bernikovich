from fastapi import FastAPI
from pydantic import BaseModel

# Создаем класс Actor с полями, используя Pydantic
class Actor(BaseModel):
    actor_id: int
    name: str
    surname: str
    age: int
    sex: str

# Создаем объект класса FastAPI
app = FastAPI()

# Создаем эндпоинт с POST запросом для приема данных о актере и их возврата
@app.post("/create_actor/")
async def create_actor(actor: Actor):
    return actor