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
    artist_category_id = Column(Integer, ForeignKey("artist_category.id"), default=None, nullable=True)
    artist_status = Column(String(255), default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())


class ArtistCategory(Base):
    __tablename__ = "artist_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


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


class SupportOrSurface(Base):
    __tablename__ = "support_or_surface"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), default=None)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


class ArtworkStyle(Base):
    __tablename__ = "artwork_style"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), default=None)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


class ArtworkCategory(Base):
    __tablename__ = "artwork_category"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), default=None)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


class Artwork(Base):
    __tablename__ = "artwork"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(100), default="Artwork Title")
    year_of_creation = Column(String(5), default=None)
    is_suitable_for_children = Column(Boolean, default=False)
    support_or_surface = Column(String(50), default=None)
    artwork_type = Column(String(20), default=None)
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
    packaging = Column(String(40), default=None)
    artwork_condition = Column(String(40), default=None)
    description = Column(String(600), default="Artwork Description")
    style = Column(String(100), default=None)
    keywords = Column(String(200), default=None)

    artist_id = Column(Integer, ForeignKey("artist.id"), nullable=True)
    artwork_category_id = Column(Integer, ForeignKey("artwork_category.id"), nullable=True)
    support_or_surface_id = Column(Integer, ForeignKey("support_or_surface.id"), nullable=True)
    artwork_style_id = Column(Integer, ForeignKey("artwork_style.id"), nullable=True)

    artwork_status = Column(String(255), default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())


class ArtworkPaintingAndDrawingTechnique(Base):
    __tablename__ = "artwork_painting_and_drawing_technique"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    artwork_id = Column(Integer, ForeignKey("artwork.id"), nullable=True)
    painting_and_drawing_technique_id = Column(Integer, ForeignKey("painting_and_drawing_technique.id"), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


class ArtworkSculptureTechnique(Base):
    __tablename__ = "artwork_sculpture_technique"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    artwork_id = Column(Integer, ForeignKey("artwork.id"), nullable=True)
    sculpture_technique_id = Column(Integer, ForeignKey("sculpture_technique.id"), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


class ArtworkHandicraftTechnique(Base):
    __tablename__ = "artwork_handicraft_technique"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    artwork_id = Column(Integer, ForeignKey("artwork.id"), nullable=True)
    handicraft_technique_id = Column(Integer, ForeignKey("handicraft_technique.id"), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


class PaintingAndDrawingTechnique(Base):
    __tablename__ = "painting_and_drawing_technique"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, default=None)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


class SculptureTechnique(Base):
    __tablename__ = "sculpture_technique"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, default=None)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())


class HandicraftTechnique(Base):
    __tablename__ = "handicraft_technique"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, default=None)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
