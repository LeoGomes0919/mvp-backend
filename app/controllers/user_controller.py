from flask import jsonify, request
from werkzeug.datastructures import MultiDict

from app.services import user_service
from app.utils import AppError, ValidationError
from app.validators.form_validator import CreateUserForm


class UserController:
    def create_user(self) -> None:
        try:
            form_data = MultiDict(request.json)
            form = CreateUserForm(form_data)

            if form.validate():
                data = form.data

                user_service.create(data)

                return jsonify({
                    'status': 'success',
                    'message': 'User created successfully',
                    'data': None
                }), 201
            else:
                errors = {field: messages[0] for field, messages in form.errors.items()}

                return jsonify({
                    'status': 'failure',
                    'message': 'Invalid inputs',
                    'data': errors
                }), 400

        except ValidationError as e:
            return jsonify({
                'status': 'failure',
                'message': 'Invalid data provided',
                'data': str(e)
            }), 409
        except Exception as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500

    def profile(self) -> tuple:
        try:

            user = user_service.profile()

            return jsonify({
                'status': 'success',
                'message': 'User found successfully',
                'data': user
            }), 200
        except ValidationError as e:
            return jsonify({
                'status': 'failure',
                'message': 'Invalid data provided',
                'data': str(e)
            }), 400
        except AppError as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500

    # TODO: Add authentication
