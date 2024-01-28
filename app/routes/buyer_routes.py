from fastapi import APIRouter, Depends

from app.schemas.buyer_schema import BuyerCreate
from app.services.buyer_service import save_buyer

router = APIRouter()


@router.post("/")
async def save(buyer_data: BuyerCreate = Depends()):
    await save_buyer(buyer_data)
    return {"success": True, "status_code": 200, "message": "Your profile was saved."}
