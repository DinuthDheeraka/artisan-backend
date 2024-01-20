import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()


class ArtistCategory(Base):
    __tablename__ = "artist_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    artist_category_status = Column(String(255), default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())
