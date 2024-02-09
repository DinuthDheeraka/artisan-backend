from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.session import engine
from app.exceptions.exceptions import handle_application_exceptions
# from app.ml.nsfw_text_detector import detect_text
from app.models.models import Base
from app.routes import buyer_routes, artist_routes, artwork_routes, user_routes, order_routes

app = FastAPI()

# Configure CORS middleware
origins = ["http://localhost:5173", ]

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"], )

# exception handlers
app.exception_handler(Exception)(handle_application_exceptions)

# buyer routes
app.include_router(buyer_routes.router, prefix="/api/v1/buyers")

# artist routes
app.include_router(artist_routes.router, prefix="/api/v1/artists")

# artist routes
app.include_router(artwork_routes.router, prefix="/api/v1/artworks")

# user routes
app.include_router(user_routes.router, prefix="/api/v1/users")

# orders routes
app.include_router(order_routes.router, prefix="/api/v1/orders")

if __name__ == "__main__":
    Base.metadata.reflect(engine)  # Reflect existing tables
    print(Base.metadata.tables)  # View reflected tables
    Base.metadata.drop_all(engine)  # Drop all tables  #
    Base.metadata.create_all(engine)  # Recreate tables
