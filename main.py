from fastapi import FastAPI

from app.db.session import engine
from app.exceptions.exceptions import handle_application_exceptions
from app.models.model import Base
from app.routes import buyer_routes, artist_routes

app = FastAPI()

# exception handlers
app.exception_handler(Exception)(handle_application_exceptions)

# buyer routes
app.include_router(buyer_routes.router, prefix="/buyers")

# artist routes
app.include_router(artist_routes.router, prefix="/artists")

if __name__ == "__main__":
    Base.metadata.reflect(engine)  # Reflect existing tables
    print(Base.metadata.tables)  # View reflected tables
    Base.metadata.drop_all(engine)  # Drop all tables  #
    Base.metadata.create_all(engine)  # Recreate tables
