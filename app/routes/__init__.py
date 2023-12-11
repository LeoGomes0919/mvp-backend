from flask import Blueprint, redirect

from .auth_routes import auth_routes_bp
from .category_routes import category_routes_bp
from .finance_routes import finance_routes_bp
from .user_routes import user_routes_bp

doc_router_bp = Blueprint('doc_router', __name__)


@doc_router_bp.get('/')
def docs():
    return redirect('/openapi/swagger')


category_routes = category_routes_bp
user_routes = user_routes_bp
finance_routes = finance_routes_bp
auth_routes = auth_routes_bp
