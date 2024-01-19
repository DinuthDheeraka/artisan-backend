import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, DateTime, func

Base = sqlalchemy.orm.declarative_base()


class Buyer(Base):
    __tablename__ = "buyer"
    id = Column(Integer, primary_key=True)
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
    buyer_status = Column(String, default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.utcnow())
    updated_at = Column(DateTime, nullable=False, server_default=func.utcnow())


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key=True)
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
    buyer_status = Column(String, default="ACTIVE")
    created_at = Column(DateTime, nullable=False, server_default=func.utcnow())
    updated_at = Column(DateTime, nullable=False, server_default=func.utcnow())
