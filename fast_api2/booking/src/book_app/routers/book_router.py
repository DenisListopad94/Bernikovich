from fastapi import APIRouter, Request

router = APIRouter(
    prefix="",
    tags=["Booking"]
)


@router.get("/{item_id}/{name}")
def get_path_params(item_id: int, name: str, ) -> dict:  # Эндпоинт, вьюшка, ручка
    return {
        "item_id": item_id,
        "name": name
    }


@router.get("/")
def get_query_params(item_id: int, name: str, ) -> dict:
    return {
        "item_id": item_id,
        "name": name
    }


@router.get("/{item_id}")
def get_query_path_params(item_id: int, name: str) -> dict:
    return {
        "item_id": item_id,
        "name": name
    }

