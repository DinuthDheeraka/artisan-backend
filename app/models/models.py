import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, DateTime, func, ForeignKey, Boolean, Float

Base = sqlalchemy.orm.declarative_base()


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    postal_code = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(255), default="NONE")
    profile_img_url = Column(String(255), default=None)
    profile_background_img_url = Column(String(255), default=None)
    biography = Column(String(500), default=None)
    artist_category = Column(String(50), nullable=True)
    artist_status = Column(String(255), default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())


class Buyer(Base):
    __tablename__ = "buyer"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    postal_code = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(255), default="NONE")
    profile_img_url = Column(String(255), default=None)
    buyer_status = Column(String(255), default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())


class Artwork(Base):
    __tablename__ = "artwork"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(100), default="Artwork Title")
    year_of_creation = Column(String(5), default=None)

    main_image = Column(String(400), default=None, nullable=True)
    image_1 = Column(String(400), default=None, nullable=True)
    image_2 = Column(String(400), default=None, nullable=True)
    image_3 = Column(String(400), default=None, nullable=True)
    image_4 = Column(String(400), default=None, nullable=True)

    artwork_category = Column(String(200), nullable=True)
    medium = Column(String(200), nullable=True)
    support_or_surface = Column(String(50), default=None)
    number_of_copies = Column(Integer, default=1, nullable=True)
    number_of_copies_for_sale = Column(Integer, default=1, nullable=True)

    can_display_outdoors = Column(Boolean, default=False)
    can_display_on_walls = Column(Boolean, default=False)
    ready_to_hang = Column(Boolean, default=False)

    is_framed = Column(Boolean, default=False)
    frame_height = Column(Float, default=0.0)
    frame_width = Column(Float, default=0.0)
    frame_thickness = Column(Float, default=0.0)

    length_unit = Column(String(10), default='cm')
    height = Column(Float, default=0.0)
    width = Column(Float, default=0.0)
    thickness = Column(Float, default=0.0)
    weight = Column(Float, default=0.0)

    sales_status = Column(String(20), default="For Sale")
    price_without_shipping = Column(Float, default=0.0)
    discount_price = Column(Float, default=0.0)

    artwork_condition = Column(String(40), default=None)
    description = Column(String(600), default="Artwork Description")
    artwork_style = Column(String(200), nullable=True)
    keywords = Column(String(200), default=None)

    artist_id = Column(Integer, ForeignKey("artist.id"), nullable=True)

    artwork_status = Column(String(255), default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())


class Review(Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    buyer_id = Column(Integer, nullable=True, default=None)
    artwork_id = Column(Integer, nullable=True, default=None)
    artist_id = Column(Integer, nullable=True, default=None)
    display_name = Column(String(255), nullable=True, default='Unknown')
    email = Column(String(255), nullable=True, default=None)
    review_comment = Column(String(255), nullable=True, default=None)
    review_img_url = Column(String(255), default=None, nullable=True)
    review_points = Column(Float, nullable=True, default=0.0)
    system_points = Column(Float, nullable=True, default=0.0)
    review_stars = Column(Integer, nullable=True, default=0.0)
    is_positive = Column(Boolean, nullable=True, default=False)
    positive_rate = Column(Float, nullable=True, default=0.0)
    review_status = Column(String(255), default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())
