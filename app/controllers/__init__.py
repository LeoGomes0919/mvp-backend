from .auth_controller import AuthController
from .category_controller import CategoryController
from .finance_controller import FinanceController
from .user_controller import UserController

category_controller = CategoryController()
user_controller = UserController()
finance_controller = FinanceController()
auth_controller = AuthController()

__all__ = ['category_controller', 'user_controller', 'finance_controller', 'auth_controller']
