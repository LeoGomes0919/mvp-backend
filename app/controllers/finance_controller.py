from flask import jsonify, request
from werkzeug.datastructures import MultiDict

from app.services import finance_service
from app.utils import AppError, ValidationError
from app.validators.form_validator import CreateFinanceForm


class FinanceController:
    def create_finance(self) -> None:
        try:
            form_data = MultiDict(request.json)
            form = CreateFinanceForm(form_data)

            if form.validate():
                data = form.data

                finance_service.create(data)

                return jsonify({
                    'status': 'success',
                    'message': 'Finance created successfully',
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
            }), 400
        except AppError as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500

    def get_by_id(self, id: str) -> tuple:
        try:
            finance = finance_service.get_by_id(id)

            return jsonify({
                'status': 'success',
                'message': 'Finance found successfully',
                'data': finance
            }), 200
        except ValidationError as e:
            return jsonify({
                'status': 'failure',
                'message': 'Invalid data provided',
                'data': str(e)
            }), 400
        except Exception as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500

    def get_by_filters(self):
        try:
            params = {
                'page': request.args.get('page', 1, type=int),
                'per_page': request.args.get('per_page', 10, type=int)
            }
            filters = request.args.to_dict()
            del filters['page']
            del filters['per_page']

            finances = finance_service.get_by_filters(filters, params)

            return jsonify({
                'status': 'success',
                'message': 'Finances found successfully',
                'data': finances
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'failure',
                'message': 'Something went wrong',
                'data': str(e)
            }), 500
