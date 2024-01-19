from fastapi import FastAPI

from app.util.db_session import SessionLocal

app = FastAPI()


@app.post("/users")
async def create_user():
    with SessionLocal() as session:
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
