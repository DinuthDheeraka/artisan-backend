from fastapi import APIRouter, Depends, UploadFile, Form

from app.ml.img_to_text import process_img
from app.ml.text_similarity_detector import similarity
from app.schemas.artwork_schema import ReviewCreate, ArtworkCreate
from app.services.artwork_service import get_all_artworks, get_art_by_id, save_artwork_review, \
    get_reviews_by_artwork_id, save_artwork

router = APIRouter()


@router.post("/")
async def save(artwork_data: ArtworkCreate = Depends()):
    await save_artwork(artwork_data)
    return {"success": True, "status_code": 200, "message": "Saved artwork successfully."}


@router.get("/")
async def get_all(category: str = "", artist_name: str = "", style: str = "", min_price: str = "", max_price: str = "",
                  search: str = ""):
    return await get_all_artworks(category=category, artist_name=artist_name, style=style, min_price=min_price,
                                  max_price=max_price, search=search)


@router.get("/{artwork_id}")
async def read_item(artwork_id: int):
    return await get_art_by_id(artwork_id)


@router.post("/reviews")
async def save_review(review_data: ReviewCreate = Depends()):
    return await save_artwork_review(review_data)


@router.get("/reviews/{artwork_id}")
async def save_review(artwork_id: int):
    return await get_reviews_by_artwork_id(artwork_id)


@router.get("/search/key-words")
async def save_review(search: str = ""):
    similarity(["mountains,monastery", search, search])


@router.post("/search/img")
async def save_review(file: UploadFile = Form(...)):
    img_data = process_img(file)
    print(img_data['text'])
    return await get_all_artworks(category="", artist_name="", style="", min_price="", max_price="",
                                  search=img_data['text'])
