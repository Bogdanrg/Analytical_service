from core.database.repository import BaseRepository
from core.database.database import db


class FoodRepository(BaseRepository):
    collection = db["food"]
