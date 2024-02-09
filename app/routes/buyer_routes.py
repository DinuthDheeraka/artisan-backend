from fastapi import APIRouter, Depends

from app.schemas.buyer_schema import BuyerCreate
from app.services.buyer_service import save_buyer

router = APIRouter()


@router.post("/")
async def save(buyer_data: BuyerCreate = Depends()):
    return await save_buyer(buyer_data)

