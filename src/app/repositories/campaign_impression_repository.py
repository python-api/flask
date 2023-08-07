from src.app.base.base_repository import BaseRepository
from src.database.models.campaign_impression import CampaignImpression
from src.database.models.campaign_request_log import CampaignRequestLog


class CampaignImpressionRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(CampaignImpression)
