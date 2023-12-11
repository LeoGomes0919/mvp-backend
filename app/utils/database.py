from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists


class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.engine = create_engine('sqlite:///finance_db.sqlite', echo=False)
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
            cls._instance.create_database_if_not_exists()
        return cls._instance

    def create_database_if_not_exists(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            self.create_tables()

    def create_tables(self):
        from app.models import BaseModel
        BaseModel.metadata.create_all(self.engine)

    def save(self, model) -> object:
        session = self.Session()
        session.add(model)
        session.commit()
        session.close()

    def get_all(self, model) -> list[object]:
        session = self.Session()
        result = session.query(model).all()
        session.close()
        return result

    def get_by_id(self, model, id) -> object:
        session = self.Session()
        result = session.query(model).get(id)
        session.close()
        return result

    def delete(self, model) -> None:
        session = self.Session()
        session.delete(model)
        session.commit()
        session.close()

    def update(self, model) -> object:
        session = self.Session()
        session.merge(model)
        session.commit()
        session.close()

    def get_by_name(self, model, name) -> object:
        session = self.Session()
        result = session.query(model).filter_by(name=name).first()
        session.close()
        return result

    def get_session(self):
        return self.Session()
