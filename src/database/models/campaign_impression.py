from sqlalchemy import Column, Integer, BigInteger, Numeric, text, String


from src.database.models import BaseModel


class CampaignImpression(BaseModel):
    __tablename__ = 'campaign_impression'
    advertiser_id = Column(Integer, index=True)
    campaign_uuid = Column(String(5000), nullable=True)