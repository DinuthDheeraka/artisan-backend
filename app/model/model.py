import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, DateTime, func
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()


class Buyer(Base):
    __tablename__ = "buyer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    display_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, default="NONE")
    profile_img_url = Column(String, default=None)
    buyer_status = Column(String, default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.utcnow())
    updated_at = Column(DateTime, nullable=False, server_default=func.utcnow())


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    display_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, default="NONE")
    profile_img_url = Column(String, default=None)
    profile_background_img_url = Column(String, default=None)
    biography = Column(String, default=None)
    artist_category_id = Column(Integer, ForeignKey="artist_category.id")
    artist_status = Column(String, default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.utcnow())
    updated_at = Column(DateTime, nullable=False, server_default=func.utcnow())

    # Relationship to the ArtistCategory
    artist_category = relationship("ArtistCategory", backref="artist")


class ArtistCategory(Base):
    __tablename__ = "artist_category"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    artist_category_status = Column(String, default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.utcnow())
    updated_at = Column(DateTime, nullable=False, server_default=func.utcnow())
