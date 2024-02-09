from fastapi import APIRouter

from app.schemas.order_schema import OrderCreate
from app.services.order_service import save_order, get_orders_by_buyer_id

router = APIRouter()


@router.post("/")
async def save(order_data: OrderCreate):
    return await save_order(order_data)


@router.get("/buyer/{buyer_id}")
async def save(buyer_id: int):
    return await get_orders_by_buyer_id(buyer_id)
