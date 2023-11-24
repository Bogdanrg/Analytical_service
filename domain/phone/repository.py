from core.database.repository import BaseRepository
from core.database.database import db


class PhoneRepository(BaseRepository):
    collection = db["phone"]
