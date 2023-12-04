from sqlalchemy import Column, String

from app.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'categories'

    name = Column(String(100), nullable=False)

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
        }
