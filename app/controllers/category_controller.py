from flask import jsonify, request
from werkzeug.datastructures import MultiDict

from app.services import category_service
from app.utils import AppError
from app.validators.form_validator import CreateCategoryForm


class CategoryController:
    def create_category(self) -> None:
        try:
            form_data = MultiDict(request.json)
            form = CreateCategoryForm(form_data)

            if form.validate():
                data = form.data

                category_service.create(data)

                return jsonify({
                    'status': 'success',
                    'message': 'Category created successfully',
                    'data': None
                }), 201
            else:
                errors = {field: messages[0] for field, messages in form.errors.items()}

                return jsonify({
                    'status': 'failure',
                    'message': 'Invalid inputs',
                    'data': errors
                }), 400
        except AppError as e:
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
        except AppError as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500
