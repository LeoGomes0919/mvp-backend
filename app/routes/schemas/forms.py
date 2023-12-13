from enum import Enum
from typing import Optional

from pydantic import BaseModel


class UserFormSchema(BaseModel):
    name: str = 'Jonh Doe'
    email: str = 'jonhdoe@gmail.com'
    password: str = '123456'


class AuthFormSchema(BaseModel):
    email: str = 'jonhdoe@gmail.com'
    password: str = '123456'


class CategoryFormSchema(BaseModel):
    name: str = 'Category 1'


class FinanceType(str, Enum):
    income = 'income'
    outcome = 'outcome'


class FinanceFormSchema(BaseModel):
    description: str = 'Description 1'
    value: float = 100.00
    finance_type: FinanceType = 'income'
    category: str = 'Category 1'


class FinanceQuerySchema(BaseModel):
    finance_id: str


class FinanceQueryFiltersSchema(BaseModel):
    page: int = 1
    per_page: int = 10
    description: Optional[str] = None
    finance_type: Optional[str] = None
