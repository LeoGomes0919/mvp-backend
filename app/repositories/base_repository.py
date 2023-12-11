from typing import List, Optional, Type

from app.models.base_model import BaseModel
from app.utils import database_manager


class BaseRepository:
    def __init__(self, model: Type[BaseModel]):
        self.model = model
        self.database_manager = database_manager
        self.session = database_manager.get_session()

    def create(self, entity: dict) -> BaseModel:
        item = self.model(**entity)
        self.database_manager.save(item)

    def get_by_id(self, entity_id: str) -> Optional[BaseModel]:
        return self.database_manager.get_by_id(self.model, entity_id)

    def get_all(self) -> List[BaseModel]:
        return self.database_manager.get_all(self.model)

    def update(self, entity: dict) -> Optional[BaseModel]:
        item = self.get_by_id(entity.id)
        for key, value in entity.items():
            setattr(item, key, value)
        self.database_manager.update(item)

        return item

    def delete(self, entity_id: str):
        item = self.get_by_id(entity_id)
        if item:
            self.database_manager.delete(item)

        self.database_manager.delete(item)
        return item.id

    def get_by_name(self, name: str) -> Optional[BaseModel]:
        return self.database_manager.get_by_name(self.model, name)
