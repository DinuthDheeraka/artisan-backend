from fastapi import UploadFile, Form


class ArtworkCreate:
    def __init__(self, title: str = Form(...), year_of_creation: str = Form(...), artwork_category: str = Form(...),
                 medium: str = Form(...), support_surface: str = Form(...), number_of_copies: int = Form(...),
                 number_of_copies_for_sale: int = Form(...), main_image: UploadFile = Form(...),
                 can_display_outdoor: bool = Form(...), can_display_on_wall: bool = Form(...),
                 ready_to_hang: bool = Form(...), is_framed: bool = Form(...), frame_height: float = Form(...),
                 frame_width: float = Form(...), frame_thickness: float = Form(...), height: float = Form(...),
                 width: float = Form(...), thickness: float = Form(...), weight: float = Form(...),
                 sales_status: str = Form(...), price_without_shipping: float = Form(...),
                 discount_price: float = Form(...), artwork_condition: str = Form(...), description: str = Form(...),
                 artwork_style: str = Form(...), keywords: str = Form(...), artist_id: int = Form(...)):
        self.title = title
        self.year_of_creation = year_of_creation
        self.artwork_category = artwork_category
        self.medium = medium
        self.support_surface = support_surface
        self.number_of_copies = number_of_copies
        self.number_of_copies_for_sale = number_of_copies_for_sale
        self.main_image = main_image
        self.can_display_outdoor = can_display_outdoor
        self.can_display_on_wall = can_display_on_wall
        self.ready_to_hang = ready_to_hang
        self.is_framed = is_framed
        self.frame_height = frame_height
        self.frame_width = frame_width
        self.frame_thickness = frame_thickness
        self.height = height
        self.width = width
        self.thickness = thickness
        self.weight = weight
        self.sales_status = sales_status
        self.price_without_shipping = price_without_shipping
        self.discount_price = discount_price
        self.artwork_condition = artwork_condition
        self.description = description
        self.artwork_style = artwork_style
        self.keywords = keywords
        self.artist_id = artist_id


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
