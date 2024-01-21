from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.util.environment import get_environment

engine = create_engine(get_environment("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
