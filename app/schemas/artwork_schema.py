from typing import Optional

from fastapi import UploadFile, Form
from pydantic import BaseModel


class ArtworkCreate(BaseModel):
    title: str = "Artwork Title"
    year_of_creation: Optional[str] = None

    main_image: Optional[str] = None
    image_1: Optional[str] = None
    image_2: Optional[str] = None
    image_3: Optional[str] = None
    image_4: Optional[str] = None

    artwork_category: Optional[str] = None
    medium: Optional[str] = None
    support_or_surface: Optional[str] = None
    number_of_copies: int = 1
    number_of_copies_for_sale: int = 1

    can_display_outdoors: bool = False
    can_display_on_walls: bool = False
    ready_to_hang: bool = False

    is_framed: bool = False
    frame_height: float = 0.0
    frame_width: float = 0.0
    frame_thickness: float = 0.0

    length_unit: str = 'cm'
    height: float = 0.0
    width: float = 0.0
    thickness: float = 0.0
    weight: float = 0.0

    sales_status: str = "For Sale"
    price_without_shipping: float = 0.0
    discount_price: float = 0.0

    artwork_condition: Optional[str] = None
    description: str = "Artwork Description"
    artwork_style: Optional[str] = None
    keywords: Optional[str] = None


class ReviewCreate:
    def __init__(self, display_name: str = Form(...), review_comment: str = Form(...),
                 review_image: UploadFile = Form(...), email: str = Form(...), review_points: int = Form(...),
                 buyer_id: int = Form(...), artwork_id: int = Form()):
        self.buyer_id = buyer_id
        self.artwork_id = artwork_id
        self.email = email
        self.display_name = display_name
        self.review_comment = review_comment
        self.review_points = review_points
        self.review_image = review_image
