from fastapi import FastAPI

from app.db.session import engine
from app.exceptions.handler import handle_application_exceptions
from app.models.artist_category_model import Base
from app.routes import buyer_routes

app = FastAPI()

# exception handlers
app.exception_handler(Exception)(handle_application_exceptions)

# routes
app.include_router(buyer_routes.router, prefix="/buyers")

if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
