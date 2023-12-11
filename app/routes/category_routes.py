from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers import category_controller

category_routes_bp = Blueprint('category_routes', __name__, url_prefix='/categories')


@category_routes_bp.post('/')
@jwt_required()
def create_category_router():
    return category_controller.create_category()


@category_routes_bp.get('/')
@jwt_required()
def get_all_categories_router():
    return category_controller.get_all_categories()
