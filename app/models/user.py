from marshmallow import fields
from sqlalchemy import Column, String
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.base_model import BaseModel, BaseModelSchema


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(256), nullable=False)

    def generate_hash(self, password: str) -> str:
        return generate_password_hash(password)

    def compare_hash(self, password: str, hashed: str) -> bool:
        return check_password_hash(hashed, password)


class UserSchema(BaseModelSchema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
