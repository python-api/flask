from sqlalchemy import text, Column, Integer, String, Boolean

from src.database.models import BaseMysqlModel, BaseModel


class TrafficSource(BaseModel):
    __tablename__ = 'traffic_source'
    __table_args__ = {'schema': 'mysql'}
    partner_id = Column(Integer, nullable=False)
    template_id = Column(Integer, nullable=False)
    cost_currency_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    is_archived = Column(Boolean, default=0, server_default=text('0'), nullable=False)
    is_postback_url = Column(Boolean, default=0, server_default=text('0'), nullable=False)
    postback_url = Column(String(2048), nullable=True)
    is_pixel_redirect_url = Column(Boolean, default=0, server_default=text('0'), nullable=False)
    pixel_redirect_url = Column(String(2048), nullable=True)
