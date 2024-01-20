import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, DateTime, func
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()


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
