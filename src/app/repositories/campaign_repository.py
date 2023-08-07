from src.app.base.base_repository import BaseRepository
from src.database.models.mysql import Campaign


class CampaignRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Campaign)