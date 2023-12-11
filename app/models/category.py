from marshmallow import fields
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel, BaseModelSchema


class Category(BaseModel):
    __tablename__ = 'categories'

    name = Column(String(100), nullable=False)


class CategorySchema(BaseModelSchema):
    name = fields.String(required=True)
