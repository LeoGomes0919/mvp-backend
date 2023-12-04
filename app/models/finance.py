
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Finance(BaseModel):
    __tablename__ = 'finances'

    description = Column(String(255), nullable=False)
    value = Column(Float, nullable=False)
    finance_type = Column(Enum('income', 'outcome'), nullable=False)
    date = Column(DateTime, nullable=False)

    # Adicionando a chave estrangeira para a tabela Category
    category_id = Column(String(36), ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', foreign_keys=[category_id])

    def as_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'value': self.value,
            'finance_type': self.finance_type,
            'date': self.date,
            'category': self.category.as_dict()
        }
