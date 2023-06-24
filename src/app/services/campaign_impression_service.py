from src.app.repositories import CampaignImpressionRepository


class CampaignImpressionService:
    def __init__(self) -> None:
        self.campaign_impression_repository = CampaignImpressionRepository()

    def list_campaign_impression(self):
        return self.campaign_impression_repository.get_all(
            columns=['id', 'advertiser_id', 'campaign_uuid']
        )
