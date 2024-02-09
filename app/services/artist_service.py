from datetime import datetime

import bcrypt
from starlette.responses import JSONResponse

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

            return {"id": new_artist.id, "email": new_artist.email, "display_name": new_artist.display_name,
                    "user_role": "Artist", "profile_img": new_artist.profile_img_url}

        except ApplicationServiceException as ae:
            session.rollback()
            return JSONResponse(status_code=ae.code,
                                content={"success": ae.success, "status_code": ae.code, "message": ae.message})

        except Exception as e:
            session.rollback()
            raise e


async def get_artist_by_id(artist_id: int):
    with (SessionLocal() as session):
        try:
            # Query the table and select only specific fields
            artist_by_id = session.query(Artist.id, Artist.display_name, Artist.profile_img_url,
                                         Artist.profile_background_img_url, Artist.artist_category,
                                         Artist.date_of_birth, Artist.biography).filter(Artist.id == artist_id).first()

            artist = {"id": artist_by_id.id, "display_name": artist_by_id.display_name,
                      "profile_img_url": artist_by_id.profile_img_url, "artist_category": artist_by_id.artist_category,
                      "date_of_birth": artist_by_id.date_of_birth,
                      "profile_background_img_url": artist_by_id.profile_background_img_url,
                      "biography": artist_by_id.biography}

            return {"artist": artist}

        except Exception as e:

            session.close()
            raise ApplicationServiceException(True, 200, 'Exception in get_all_artworks')

        finally:
            session.close()
