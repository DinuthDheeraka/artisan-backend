from fastapi import APIRouter, Depends

from app.schemas.artist_schema import ArtistCreate
from app.services.artist_service import save_artist

router = APIRouter()


@router.post("/")
async def save(artist_data: ArtistCreate = Depends()):
    await save_artist(artist_data)
    return {"success": True, "status_code": 200, "message": "Your profile was saved."}
