from datetime import datetime

import bcrypt
from starlette.responses import JSONResponse

from app.db.session import SessionLocal
from app.models.models import Buyer
from app.util.s3_file_uploader import upload_to_s3


async def save_buyer(buyer_data):
    with SessionLocal() as session:
        try:
            # check if email is already exists
            user_by_email = session.query(Buyer).filter_by(email=buyer_data.email, buyer_status="ACTIVE").first()

            if user_by_email is not None:
                return JSONResponse(status_code=200, content={"success": False, "status_code": 200,
                                                              "message": "Email is already exists!"})

            # bcrypt password
            hashed_password = bcrypt.hashpw(buyer_data.password.encode(), bcrypt.gensalt())

            # upload profile image
            object_name = (f"uploads/profile-images/{datetime.utcnow()}{'_'}"
                           f"{buyer_data.profile_image.filename}")

            profile_img_url = upload_to_s3(object_name, buyer_data.profile_image.file)

            # save new buyer
            new_buyer = Buyer(email=buyer_data.email, password=hashed_password, full_name=buyer_data.full_name,
                              display_name=buyer_data.display_name, address=buyer_data.address, city=buyer_data.city,
                              postal_code=buyer_data.postal_code, phone_number=buyer_data.phone_number,
                              date_of_birth=buyer_data.date_of_birth, gender=buyer_data.gender,
                              profile_img_url=profile_img_url)

            session.add(new_buyer)

            session.commit()

            user = {"id": new_buyer.id, "email": new_buyer.email, "display_name": new_buyer.display_name,
                    "user_role": "Buyer", "profile_img": new_buyer.profile_img_url}

            return {"user": user, "success": True, "status_code": 200, "message": "Your profile was saved."}

        except Exception as e:
            session.rollback()
            raise e
