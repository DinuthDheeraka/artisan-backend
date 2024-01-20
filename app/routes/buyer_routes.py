from fastapi import APIRouter

from app.schemas.buyer_schema import BuyerCreate
from app.service.buyer_service import save_buyer

router = APIRouter()


@router.post("/")
async def save(buyer_data: BuyerCreate):
    await save_buyer(buyer_data)
