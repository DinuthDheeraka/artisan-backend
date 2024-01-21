from fastapi import APIRouter

from app.schemas.artist_schema import ArtistCreate
from app.services.artist_service import save_artist

router = APIRouter()


@router.post("/")
async def save(artist_data: ArtistCreate):
    await save_artist(artist_data)
