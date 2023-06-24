from src.app.base.base_repository import BaseRepository
from src.database.models import CampaignImpression


class CampaignImpressionRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(CampaignImpression)
