from datetime import datetime
from uuid import uuid4 as uuid

from marshmallow import Schema, fields
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BaseModelSchema(Schema):
    id = fields.UUID(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
