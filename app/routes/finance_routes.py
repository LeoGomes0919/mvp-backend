from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from app.controllers import finance_controller

from .schemas import *

user_tag = Tag(name='Finances', description="Create, list, update and delete finances")
finance_routes_bp = APIBlueprint('finance_routes', __name__, url_prefix='/finances',
                                 abp_tags=[user_tag], abp_security=[{'jwt': []}], abp_responses={
                                     401: ErrorUnauthorizedResponseSchema
                                 })


@finance_routes_bp.post('/', responses={201: SuccessCreatedResponseSchema, 400: ErrorFieldResponseSchema})
@jwt_required()
def create_finance_router(body: FinanceFormSchema):
    """Create a new finance"""
    return finance_controller.create_finance(body)


@finance_routes_bp.get('/filters', responses={200: FinanceListResponseSchema})
@jwt_required()
def get_finance_by_filters_router(query: FinanceQueryFiltersSchema):
    """Get finances by filters description, finance_type= ENTRADAS | SAIDAS, page and per_page"""
    return finance_controller.get_by_filters(query)


@finance_routes_bp.get('/<finance_id>', responses={200: FinanceResponseSchema, 400: FinanceNotFoundResponseSchema})
@jwt_required()
def get_finance_by_id_router(path: FinanceQuerySchema):
    """Get finance by id"""
    return finance_controller.get_by_id(path)


@finance_routes_bp.put('/<finance_id>', responses={200: SuccessUpdatedResponseSchema, 400: ErrorFieldResponseSchema})
@jwt_required()
def update_finance_router(body: FinanceFormSchema, path: FinanceQuerySchema):
    """Update finance by id"""
    return finance_controller.update_finance(body, path)


@finance_routes_bp.delete('/<finance_id>', responses={200: SuccessDeletedResponseSchema})
@jwt_required()
def delete_finance_router(path: FinanceQuerySchema):
    """Delete finance by id"""
    return finance_controller.delete_finance(path)
