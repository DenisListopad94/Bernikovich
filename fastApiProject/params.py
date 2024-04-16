from fastapi import FastAPI

# Создаем объект класса FastAPI
app = FastAPI()

# Эндпоинт для передачи данных через path params (item_id - int)
@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    return {"item_id": item_id}

# Эндпоинт для передачи данных через query params (int_param - int, str_param - str)
@app.get("/items/")
async def get_item_by_params(int_param: int, str_param: str):
    return {"int_param": int_param, "str_param": str_param}

# Эндпоинт для передачи данных через path params (str_param - str) и query params (int_param1 - int, int_param2 - int)
@app.get("/items/{str_param}")
async def get_item_by_mix_params(str_param: str, int_param1: int, int_param2: int):
    return {"str_param": str_param, "int_param1": int_param1, "int_param2": int_param2}