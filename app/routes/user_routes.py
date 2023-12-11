from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers import user_controller

user_routes_bp = Blueprint('user_routes', __name__, url_prefix='/users')


@user_routes_bp.post('/')
def create_user_router():
    return user_controller.create_user()


@user_routes_bp.get('/profile')
@jwt_required()
def profile_router():
    return user_controller.profile()
