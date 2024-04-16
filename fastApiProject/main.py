from typing import Union
import random
from fastapi import FastAPI

app = FastAPI()

# Эндпоинт для получения списка из 5 случайных чисел
@app.get("/random_numbers/")
async def get_random_numbers():
    # Генерируем список из 5 случайных чисел
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    return {"random_numbers": random_numbers}
