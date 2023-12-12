from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from app.controllers import category_controller

from .schemas import *

category_tag = Tag(name='Categories', description="Create and list categories")
category_routes_bp = APIBlueprint('category_routes', __name__, url_prefix='/categories',
                                  abp_tags=[category_tag], abp_security=[{'jwt': []}])


@category_routes_bp.post('/', responses={201: SuccessCreatedResponseSchema, 400: ErrorFieldResponseSchema,
                                         401: ErrorUnauthorizedResponseSchema},)
@jwt_required()
def create_category_router(body: CategoryFormSchema):
    """Create a new category"""
    return category_controller.create_category(body)


@category_routes_bp.get('/', responses={200: CategoriesRepsonseSchema, 500: ErrorResponseSchema,
                                        401: ErrorUnauthorizedResponseSchema})
@jwt_required()
def get_all_categories_router():
    """Get all categories"""
    return category_controller.get_all_categories()
