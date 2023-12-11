from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from app.routes import auth_routes, category_routes, finance_routes, user_routes

from .config import app_config, default_config
from .utils import jwt


def create_app(config_name=None):
    app = Flask(__name__)
    jwt.init_app(app)

    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Finance API"
        }
    )

    config_name = config_name or default_config
    app.config.from_object(app_config[config_name])

    # Register blueprints routes
    app.register_blueprint(swaggerui_blueprint, uxrl_prefix=SWAGGER_URL)
    app.register_blueprint(auth_routes)
    app.register_blueprint(category_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(finance_routes)

    return app
