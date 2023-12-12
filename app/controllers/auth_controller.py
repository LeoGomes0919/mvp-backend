from flask import jsonify
from werkzeug.datastructures import MultiDict

from app.routes.schemas import *
from app.services import auth_service
from app.utils import ValidationError


class AuthController:
    def login(self, form: AuthFormSchema) -> tuple:
        try:
            data = MultiDict(form)
            tokens = auth_service.auth_user(data)

            return jsonify({
                'status': 'success',
                'message': 'User authenticated successfully',
                'data': tokens
            }), 200
        except ValidationError as e:
            return jsonify({
                'status': 'failure',
                'message': 'Invalid data provided',
                'data': str(e)
            }), e.code
        except Exception as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500
