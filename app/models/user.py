from sqlalchemy import Column, String

from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }
