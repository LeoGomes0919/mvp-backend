from flask import jsonify
from werkzeug.datastructures import MultiDict

from app.routes.schemas import *
from app.services import user_service
from app.utils import ValidationError
from app.validators.form_validator import UserForm


class UserController:
    def create_user(self, form: UserFormSchema) -> None:
        try:
            data = MultiDict(form)

            validate = UserForm(data)

            if not validate.validate():
                return jsonify({
                    'status': 'failure',
                    'message': 'Invalid data provided',
                    'data': validate.errors
                }), 400

            user_service.create(validate.data)

            return jsonify({
                'status': 'success',
                'message': 'User created successfully',
                'data': None
            }), 201

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
            }), e.code
        except Exception as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500
