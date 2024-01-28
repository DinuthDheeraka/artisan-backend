from fastapi import APIRouter

from app.schemas.user_schema import UserLogin
from app.services.user_service import user_login

router = APIRouter()


@router.post("/login")
async def login(user_data: UserLogin):
    return await user_login(user_data)
