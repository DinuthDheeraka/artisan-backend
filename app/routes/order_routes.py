from fastapi import APIRouter

from app.schemas.order_schema import OrderCreate
from app.services.order_service import save_order

router = APIRouter()


@router.post("/")
async def save(order_data: OrderCreate):
    return await save_order(order_data)
