from app.db.session import SessionLocal


async def user_login(user_data):
    with SessionLocal() as session:
        try:
            return {'user_data': user_data}
        except Exception as e:
            session.rollback()
            raise e
