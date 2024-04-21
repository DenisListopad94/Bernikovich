from fastapi import APIRouter

from flask import Blueprint
router = APIRouter()


user_router = Blueprint('user', __name__)

@user_router.route('/user')
def user():
    return 'User page'
@router.get("/users")
async def get_users():
    return {"message": "List of users"}

