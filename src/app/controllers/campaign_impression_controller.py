from src.app.response import CampaignImpressionResponse
from src.app.response.traffic_source_response import TrafficSourceResponse
from src.app.services import CampaignImpressionService
from src.helpers import MakeResponse
from src.helpers.exception_handler import ExceptionHandler


class CampaignImpressionController:
    def __init__(self) -> None:
        self.campaign_impression_service = CampaignImpressionService()

    @ExceptionHandler().error_handler
    def list_campaign_impression(self):
        campaign_impression = self.campaign_impression_service.list_campaign_impression()
        campaign_impression = TrafficSourceResponse(many=True).dump(campaign_impression)
        return MakeResponse.success({'items': campaign_impression})
