from sqlalchemy import func

from app.models import Category
from app.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)

    def get_by_name(self, name: str) -> Category:
        return self.session.query(Category).filter(func.lower(Category.name) == name.lower()).first()

    def find_or_create(self, name: str) -> Category:
        category = self.get_by_name(name)

        if not category:
            category = Category(name=name)
            self.session.add(category)
            self.session.commit()

        return category
