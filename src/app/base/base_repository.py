from sqlalchemy.orm import load_only

from src import database, db


class BaseRepository:
    def __init__(self, model) -> None:
        self.model = model
        super().__init__()

    def get_object(self, conditions:list, columns=[]):
        load_columns = [getattr(self.model, col) for col in columns] if columns else [self.model]
        return (database.session
            .query(*load_columns)
            .filter(*conditions)
            .options(load_only(*columns))
            .first()
        )


    def get_all(self, columns=[], conditions=[]):
        load_columns = [getattr(self.model, col) for col in columns] if columns else [self.model]

        return (db.session
            .query(*load_columns)
            .filter(*conditions)
            .all()
        )