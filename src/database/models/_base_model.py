from sqlalchemy import Column, Integer

from src import db


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, nullable=False)

    @classmethod
    def from_json(cls, json):
        data = {k: v for k, v in json.items() if hasattr(cls, k)}
        return cls(**data)


class BaseMysqlModel(BaseModel):
    __table_args__ = {'schema': 'mysql'}
