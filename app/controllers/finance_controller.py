from flask import jsonify, request
from werkzeug.datastructures import MultiDict

from app.routes.schemas import *
from app.services import finance_service
from app.utils import ValidationError
from app.validators.form_validator import FinanceForm


class FinanceController:
    def create_finance(self, form: FinanceFormSchema) -> None:
        try:
            data = MultiDict(form)
            validate = FinanceForm(data)

            if not validate.validate():
                return jsonify({
                    'status': 'failure',
                    'message': 'Invalid data provided',
                    'data': validate.errors
                }), 400

            finance_service.create(validate.data)

            return jsonify({
                'status': 'success',
                'message': 'Finance created successfully',
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

    def get_by_id(self, query: FinanceQuerySchema) -> tuple:
        try:
            finance = finance_service.get_by_id(query.finance_id)

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

    def get_by_filters(self, query: FinanceQueryFiltersSchema):
        try:
            query_params = MultiDict(query)
            pagination = {
                'page': query_params.get('page', 1, type=int),
                'per_page': query_params.get('per_page', 10, type=int)
            }
            filters = query_params
            del filters['page']
            del filters['per_page']

            finances = finance_service.get_by_filters(filters, pagination)

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

    def update_finance(self, body: FinanceFormSchema, query: FinanceQuerySchema) -> None:
        try:
            form = MultiDict(body)
            validate = FinanceForm(form)

            if not validate.validate():
                return jsonify({
                    'status': 'failure',
                    'message': 'Invalid data provided',
                    'data': validate.errors
                }), 400

            finance_service.update(query.finance_id, validate.data)

            return jsonify({
                'status': 'success',
                'message': 'Finance updated successfully',
                'data': None
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

    def delete_finance(self, query: FinanceQuerySchema) -> None:
        try:
            finance_service.delete(query.finance_id)

            return jsonify({
                'status': 'success',
                'message': 'Finance deleted successfully',
                'data': None
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
