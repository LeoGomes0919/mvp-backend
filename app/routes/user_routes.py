from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from app.controllers import user_controller

from .schemas import *

user_tag = Tag(name='Users', description="Create a new user and get profile")
user_routes_bp = APIBlueprint('user_routes', __name__, url_prefix='/users', abp_tags=[user_tag])


@user_routes_bp.post('/', responses={201: SuccessCreatedResponseSchema, 400: ErrorFieldResponseSchema})
def create_user_router(body: UserFormSchema):
    """Add a new user."""
    return user_controller.create_user(body)


@user_routes_bp.get('/profile', responses={
    200: ProfileRepsonseSchema, 401:
        ErrorUnauthorizedResponseSchema}, security=[{'jwt': []}])
@jwt_required()
def profile_router():
    """Get logged in user profile."""
    return user_controller.profile()
