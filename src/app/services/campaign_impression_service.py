from src.app.repositories import CampaignImpressionRepository
from src.app.repositories.campaign_repository import CampaignRepository
from src.app.repositories.campaign_request_log_repository import CampaignRequestLogRepository
from src.app.repositories.traffic_source_repository import TrafficSourceRepository


class CampaignImpressionService:
    def __init__(self) -> None:
        self.campaign_impression_repository = CampaignImpressionRepository()
        self.campaign_request_log_repository = CampaignRequestLogRepository()
        self.campaign_repository = CampaignRepository()
        self.traffic_source_repository = TrafficSourceRepository()

    def list_campaign_impression(self):
        campaign_impression =  self.campaign_impression_repository.get_all()

        campaign_uuid = [item.campaign_uuid for item in campaign_impression]


        if campaign_impression:
            campaign_request_log =  self.campaign_impression_repository.get_all(
                conditions=[
                    self.campaign_repository.model.uuid.in_(campaign_uuid)
                ]
            )








        # campaign = self.campaign_repository.get_all(
        #     conditions=[
        #         self.campaign_repository.model.uuid.in_(campaign_uuid)
        #     ]
        # )

        # traffic_source_ids = [item.traffic_source_id for item in campaign]
        #
        # traffic_source = self.traffic_source_repository.get_all(
        #     conditions=[
        #         self.traffic_source_repository.model.id.in_(traffic_source_ids)
        #     ]
        # )

            return campaign_request_log
