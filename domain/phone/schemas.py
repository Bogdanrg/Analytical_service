from decimal import Decimal

from pydantic import BaseModel


class PhoneModel(BaseModel):
    id: str
    name: str
    price: Decimal
    onMarket: bool
    description: str
    count: int

