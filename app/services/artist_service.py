from datetime import datetime

import bcrypt

from app.db.session import SessionLocal
from app.exceptions.exceptions import ApplicationServiceException
from app.models.models import Artist
from app.util.s3_file_uploader import upload_to_s3


async def save_artist(artist_data):
    with SessionLocal() as session:
        try:
            # check if email is already exists
            user_by_email = session.query(Artist).filter_by(email=artist_data.email, artist_status="ACTIVE").first()

            if user_by_email is not None:
                raise ApplicationServiceException(False, 200, "Email already registered")

            # bcrypt password
            hashed_password = bcrypt.hashpw(artist_data.password.encode(), bcrypt.gensalt())

            # upload profile image
            object_name = (f"uploads/profile-images/{datetime.utcnow()}{'_'}"
                           f"{artist_data.profile_image.filename}")

            profile_img_url = upload_to_s3(object_name, artist_data.profile_image.file)

            # save new buyer
            new_artist = Artist(email=artist_data.email, password=hashed_password, full_name=artist_data.full_name,
                                display_name=artist_data.display_name, address=artist_data.address,
                                city=artist_data.city, postal_code=artist_data.postal_code,
                                phone_number=artist_data.phone_number, date_of_birth=artist_data.date_of_birth,
                                gender=artist_data.gender, biography=artist_data.biography,
                                artist_category=artist_data.categories, profile_img_url=profile_img_url)

            session.add(new_artist)

            session.commit()

        except Exception as e:
            session.rollback()
            raise e
