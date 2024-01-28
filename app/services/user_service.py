import bcrypt

from app.db.session import SessionLocal
from app.models.models import Artist, Buyer


async def user_login(user_data):
    with SessionLocal() as session:
        try:

            artist_by_email = session.query(Artist).filter_by(email=user_data.email, artist_status="ACTIVE").first()

            buyer_by_email = session.query(Buyer).filter_by(email=user_data.email, buyer_status="ACTIVE").first()

            if artist_by_email is None and buyer_by_email is None:
                return {"success": False, "status": 200, "message": "Invalid email or password"}

            if artist_by_email is not None:

                if bcrypt.checkpw(user_data.password.encode(), artist_by_email.password.encode()):
                    return {"success": True, "status": 200, "message": "Authenticated user successfully.",
                            "user": {"id": artist_by_email.id, "email": artist_by_email.email,
                                     "display_name": artist_by_email.display_name,
                                     "profile_img": artist_by_email.profile_img_url, "user_role": "Artist"}}

            if buyer_by_email is not None:

                if bcrypt.checkpw(user_data.password.encode(), buyer_by_email.password.encode()):
                    return {"success": True, "status": 200, "message": "Authenticated user successfully.",
                            "user": {"id": buyer_by_email.id, "email": buyer_by_email.email,
                                     "display_name": buyer_by_email.display_name,
                                     "profile_img": buyer_by_email.profile_img_url, "user_role": "Buyer"}}

            return {"success": False, "status": 200, "message": "Invalid email or password"}

        except Exception as e:
            session.rollback()
            raise e
