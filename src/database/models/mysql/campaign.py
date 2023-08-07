from sqlalchemy import Column, Integer, Boolean, text, String, Numeric

from src.database.models import BaseMysqlModel, BaseModel


class Campaign(BaseModel):
    __tablename__ = 'campaign'
    __table_args__ = {'schema': 'mysql'}
    uuid = Column(String(32), unique=True, nullable=False)
    partner_id = Column(Integer, nullable=False)
    traffic_source_id = Column(Integer, nullable=False)
    country_id = Column(Integer, server_default=text('0'), nullable=False)
    name = Column(String(255), nullable=False)
    is_archived = Column(Boolean, default=0, server_default=text('0'), nullable=False)
    cost_model_id = Column(Integer, nullable=False, comment='1:NOT_TRACKED / 2: CPC / 3: CPM')
    cost_value = Column(Numeric(20, 6), nullable=True)
    path_destination_id = Column(Integer, nullable=False, comment='1:ONLY_OFFER / 2: LANDERS_AND_OFFERS')
    transition_type_id = Column(Integer, nullable=False, comment='1:OFFER_DIRECT / 2: OFFER_REDIRECT_302 / 3: LANDER_OFFER_DIRECT / 4: LANDER_OFFER_META_REFRESH / 5: LANDER_OFFER_DOUBLE_META_REFRESH')
    is_distribution = Column(Boolean, default=0, server_default=text('0'), nullable=False)
    impression_url = Column(String(2048), nullable=False)
