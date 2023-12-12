from flask_openapi3 import APIBlueprint, Tag

from app.controllers import auth_controller

from .schemas import *

auth_tag = Tag(name='Auth', description="Login in the application")
auth_routes_bp = APIBlueprint('auth_routes', __name__, url_prefix='/auth', abp_tags=[auth_tag])


@auth_routes_bp.post('/login', responses={200: SuccessLoginResponseSchema, 400: ErrorLoginResponseSchema})
def create_category_router(body: AuthFormSchema):
    """Login in the application."""
    return auth_controller.login(body)
