from pydantic import BaseModel


class BuyerCreate(BaseModel):
    email: str
    password = str
    full_name = str
    display_name = str
    address = str
    city = str
    postal_code = str
    phone_number = str
    date_of_birth = str
    gender = str
    buyer_status = str
