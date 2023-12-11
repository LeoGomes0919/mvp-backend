from typing import List, Optional, Type

from app.models.base_model import BaseModel
from app.utils import database_manager


class BaseRepository:
    def __init__(self, model: Type[BaseModel]):
        self.model = model
        self.database_manager = database_manager
        self.session = database_manager.get_session()

    def create(self, entity: dict) -> None:
        item = self.model(**entity)
        self.database_manager.save(item)

    def get_by_id(self, entity_id: str) -> Optional[BaseModel]:
        return self.database_manager.get_by_id(self.model, entity_id)

    def get_all(self) -> List[BaseModel]:
        return self.database_manager.get_all(self.model)

    def update(self, entity: dict) -> None:
        item = self.model(**entity)
        self.database_manager.update(item)

    def delete(self, entity: str):
        self.database_manager.delete(entity)

    def get_by_name(self, name: str) -> Optional[BaseModel]:
        return self.database_manager.get_by_name(self.model, name)
