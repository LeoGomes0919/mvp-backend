
from marshmallow import fields
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel, BaseModelSchema


class Finance(BaseModel):
    __tablename__ = 'finances'

    description = Column(String(255), nullable=False)
    value = Column(Float, nullable=False)
    finance_type = Column(Enum('income', 'outcome'), nullable=False)
    date = Column(DateTime, nullable=False)

    # Adicionando a chave estrangeira para a tabela Category
    category_id = Column(String(36), ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', foreign_keys=[category_id], lazy='joined')

    # Adicionando a chave estrangeira para a tabela User
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    user = relationship('User', foreign_keys=[user_id], lazy='joined')


class FinanceSchema(BaseModelSchema):
    description = fields.String(required=True)
    value = fields.Float(required=True)
    finance_type = fields.String(required=True)
    date = fields.DateTime(required=True)
    category = fields.Nested({
        'id': fields.String(required=True),
        'name': fields.String(required=True)
    }, required=True)
