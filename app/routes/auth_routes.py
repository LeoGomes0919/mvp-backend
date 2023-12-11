from flask import Blueprint

from app.controllers import auth_controller

auth_routes_bp = Blueprint('auth_routes', __name__, url_prefix='/auth')


@auth_routes_bp.post('/login')
def create_category_router():
    return auth_controller.login()
