from flask import jsonify, request
from werkzeug.datastructures import MultiDict

from app.routes.schemas import *
from app.services import category_service
from app.validators.form_validator import CategoryForm


class CategoryController:
    def create_category(self, form: CategoryFormSchema) -> None:
        try:
            data = MultiDict(form)
            validate = CategoryForm(data)

            if not validate.validate():
                return jsonify({
                    'status': 'failure',
                    'message': 'Invalid data provided',
                    'data': validate.errors
                }), 400

            category_service.create(validate.data)

            return jsonify({
                'status': 'success',
                'message': 'Category created successfully',
                'data': None
            }), 201

        except Exception as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500

    def get_all_categories(self) -> tuple:
        try:
            categories = category_service.get_all()

            return jsonify({
                'status': 'success',
                'message': 'Categories found successfully',
                'data': categories
            }), 200

        except Exception as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500
