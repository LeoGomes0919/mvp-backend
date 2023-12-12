from flask import Flask
from flask_openapi3 import Info, OpenAPI

from app.routes import auth_routes, category_routes, finance_routes, user_routes

from .config import app_config, default_config
from .utils import jwt

info = Info(title=".Finance API", description="A simple API to manage your finances", version="1.0.0", contact={
    "name": "Leonardo Gomes",
    "email": "leonardogs0919@gmail.com"
})

security_schemes = {
    "jwt": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    }
}


def create_app(config_name=None):
    app = Flask(__name__)

    app = OpenAPI(__name__, info=info, security_schemes=security_schemes)
    jwt.init_app(app)

    config_name = config_name or default_config
    app.config.from_object(app_config[config_name])

    # Register blueprints routes
    app.register_api(auth_routes)
    app.register_api(category_routes)
    app.register_api(user_routes)
    app.register_api(finance_routes)

    return app
