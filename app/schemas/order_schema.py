from pydantic import BaseModel


class OrderCreate(BaseModel):
    buyer_id: int
    cart: list
