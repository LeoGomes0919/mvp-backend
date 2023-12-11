from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers import finance_controller

finance_routes_bp = Blueprint('finance_routes', __name__, url_prefix='/finances')


@finance_routes_bp.post('/')
@jwt_required()
def create_finance_router():
    return finance_controller.create_finance()


@finance_routes_bp.get('/<finance_id>')
@jwt_required()
def get_finance_by_id_router(finance_id):
    return finance_controller.get_by_id(finance_id)


@finance_routes_bp.get('/')
@jwt_required()
def get_finance_by_filters_router():
    return finance_controller.get_by_filters()
