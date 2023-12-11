from flask import jsonify, request

from app.services import auth_service
from app.utils import AppError, ValidationError


class AuthController:
    def login(self) -> tuple:
        try:
            data = request.get_json()

            tokens = auth_service.auth_user(data)

            return jsonify({
                'status': 'success',
                'message': 'User authenticated successfully',
                'data': tokens
            }), 200
        except ValidationError as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 400
        except Exception as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500
