from src.app.base.base_repository import BaseRepository
from src.database.models.mysql import Campaign, TrafficSource


class TrafficSourceRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(TrafficSource)