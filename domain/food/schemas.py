from decimal import Decimal
from pydantic import BaseModel


class FoodModel(BaseModel):
    id: str
    name: str
    calories: Decimal
    description: str
    count: int
