from app.models import Category, CategorySchema
from app.repositories import category_repository
from app.utils import logger


class CategoryService:
    def __init__(self):
        self.logger = logger
        self.category_repository = category_repository

    def create(sefl, data: dict) -> Category:
        sefl.logger.info('[CategoryService]: Creating category: {data}')
        return sefl.category_repository.create(data)

    def get_all(self) -> list[Category]:
        self.logger.info('[CategoryService]: Getting all categories')
        categories = self.category_repository.get_all()
        categories_schema = CategorySchema(many=True)

        return categories_schema.dump(categories)
