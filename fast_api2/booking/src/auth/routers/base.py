from fastapi import APIRouter, FastAPI
from src.auth.routers.auth_router import router as user_router

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(user_router)


@router.get("/")
async def get_base():
    return {"message": "Hello from base router"}
