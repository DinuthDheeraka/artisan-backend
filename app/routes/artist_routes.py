from fastapi import APIRouter, Depends

from app.schemas.artist_schema import ArtistCreate
from app.services.artist_service import save_artist, get_artist_by_id

router = APIRouter()


@router.post("/")
async def save(artist_data: ArtistCreate = Depends()):
    user_data = await save_artist(artist_data)
    return {"user": user_data, "success": True, "status_code": 200, "message": "Your profile was saved."}


@router.get("/{artist_id}")
async def save(artist_id: int):
    return await get_artist_by_id(artist_id)
