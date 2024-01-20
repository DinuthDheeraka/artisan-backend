import bcrypt

from app.db.session import SessionLocal
from app.exceptions.application_service_exception import ApplicationServiceException
from app.models.buyer_model import Buyer


async def save_buyer(buyer_data):
    with SessionLocal() as session:
        try:
            # check if email is already exists
            user_by_email = session.query(Buyer).filter_by(email=buyer_data.email, buyer_status="ACTIVE").first()

            if user_by_email is not None:
                raise ApplicationServiceException(False, 200, "email already registered")

            # bcrypt password
            hashed_password = bcrypt.hashpw(buyer_data.password.encode(), bcrypt.gensalt())

            # save new buyer
            new_buyer = Buyer(email=buyer_data.email, password=hashed_password, full_name=buyer_data.full_name,
                              display_name=buyer_data.display_name, address=buyer_data.address, city=buyer_data.city,
                              postal_code=buyer_data.postal_code, phone_number=buyer_data.phone_number,
                              date_of_birth=buyer_data.date_of_birth, gender=buyer_data.gender)
            session.add(new_buyer)

            session.commit()

        except Exception as e:
            session.rollback()
            raise e
