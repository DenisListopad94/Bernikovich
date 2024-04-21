from fastapi import APIRouter, FastAPI
from src.book_app.routers.book_router import router as booking_router


router = APIRouter(
    prefix="/books",
    tags=["Booking"]
)

router.include_router(booking_router)