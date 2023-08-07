from sqlalchemy import Column, Integer, BigInteger, Numeric, text, String


from src.database.models import BaseModel


class CampaignRequestLog(BaseModel):
    __tablename__ = 'campaign_request_log'
    campaign_uuid = Column(String(255), index=True)
