from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:1234@127.0.0.1:3306/the_artisan")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
