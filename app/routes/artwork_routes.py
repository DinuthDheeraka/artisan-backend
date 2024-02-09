from fastapi import APIRouter, Depends

from app.schemas.artwork_schema import ReviewCreate, ArtworkCreate
from app.services.artwork_service import get_all_artworks, get_art_by_id, save_artwork_review, \
    get_reviews_by_artwork_id, save_artwork

router = APIRouter()


@router.post("/")
async def save(artwork_data: ArtworkCreate = Depends()):
    await save_artwork(artwork_data)
    return {"success": True, "status_code": 200, "message": "Saved artwork successfully."}


@router.get("/")
async def get_all(category: str = "", artist_name: str = "", style: str = "", min_price: str = "", max_price: str = ""):
    return await get_all_artworks(category=category, artist_name=artist_name, style=style, min_price=min_price,
                                  max_price=max_price)


@router.get("/{artwork_id}")
async def read_item(artwork_id: int):
    return await get_art_by_id(artwork_id)


@router.post("/reviews")
async def save_review(review_data: ReviewCreate = Depends()):
    return await save_artwork_review(review_data)


@router.get("/reviews/{artwork_id}")
async def save_review(artwork_id: int):
    return await get_reviews_by_artwork_id(artwork_id)
