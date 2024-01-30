from fastapi import APIRouter, Depends

from app.schemas.artwork_schema import ArtworkCreate, ReviewCreate
from app.services.artwork_service import save_artwork, get_all_artworks, get_art_by_id, save_artwork_review, \
    get_reviews_by_artwork_id

router = APIRouter()


@router.post("/")
async def save(artwork_data: ArtworkCreate):
    await save_artwork(artwork_data)


@router.get("/")
async def get_all():
    return await get_all_artworks()


@router.get("/{artwork_id}")
async def read_item(artwork_id: int):
    return await get_art_by_id(artwork_id)


@router.post("/reviews")
async def save_review(review_data: ReviewCreate = Depends()):
    return await save_artwork_review(review_data)


@router.get("/reviews/{artwork_id}")
async def save_review(artwork_id: int):
    return await get_reviews_by_artwork_id(artwork_id)
