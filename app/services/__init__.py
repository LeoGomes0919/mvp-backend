from .auth_service import AuthService
from .category_service import CategoryService
from .finance_service import FinanceService
from .user_service import UserService

category_service = CategoryService()
user_service = UserService()
finance_service = FinanceService()
auth_service = AuthService()

__all__ = ['category_service', 'user_service', 'finance_service', 'auth_service']
