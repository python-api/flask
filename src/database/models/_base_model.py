from sqlalchemy import Column, Integer

from src import database


class BaseModel(database.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, nullable=False)

    @classmethod
    def from_json(cls, json):
        data = {k: v for k, v in json.items() if hasattr(cls, k)}
        return cls(**data)