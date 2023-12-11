from .category_repository import CategoryRepository
from .finance_repository import FinanceRepository
from .user_repository import UserRepository

category_repository = CategoryRepository()
user_repository = UserRepository()
finance_repository = FinanceRepository()

__all__ = ['category_repository', 'user_repository', 'finance_repository']
