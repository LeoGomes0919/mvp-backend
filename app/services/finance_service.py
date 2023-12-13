from datetime import datetime

from flask_jwt_extended import get_jwt_identity

from app.models import Finance, FinanceSchema
from app.repositories import category_repository, finance_repository, user_repository
from app.utils import ValidationError, logger


class FinanceService:
    def __init__(self):
        self.logger = logger
        self.finance_repository = finance_repository
        self.category_repository = category_repository
        self.user_repository = user_repository
        self

    def create(self, data: dict) -> Finance:
        self.logger.info('[FinanceService]: Creating finance: {data}')

        sub = get_jwt_identity()
        user_id = sub.get('user_id')

        if not user_id:
            raise ValidationError('Error on create finance unauthorized', 401)

        category = self.category_repository.find_or_create(data.get('category'))

        if not category:
            raise ValidationError('Error on create finance category not found')

        now = datetime.now()
        data.update({'date': now, 'user_id': user_id, 'category_id': category.id})
        del data['category']

        self.finance_repository.create(data)

    def update(self, id: str, data: dict) -> None:
        self.logger.info('[FinanceService]: Updating finance: {id}')
        finance = self.finance_repository.get_by_id(id)

        if not finance:
            raise ValidationError('Error on update finance')

        category = self.category_repository.find_or_create(data.get('category'))

        if not category:
            raise ValidationError('Error on update finance category not found')

        data.update({'date': finance.date, 'id': id, 'category_id': category.id})
        del data['category']

        self.finance_repository.update(data)

    def delete(self, id: str) -> None:
        self.logger.info('[FinanceService]: Deleting finance: {id}')
        finance = self.finance_repository.get_by_id(id)

        if not finance:
            raise ValidationError('Error on delete finance not found')

        return self.finance_repository.delete(finance)

    def get_by_filters(self, filters: dict, pagination: dict):
        self.logger.info('[FinanceService]: Getting all finances')

        if filters.get('finance_type'):
            if filters.get('finance_type') == 'entradas':
                filters['finance_type'] = 'income'
            else:
                filters['finance_type'] = 'outcome'

        sub = get_jwt_identity()
        user_id = sub.get('user_id')

        filters.update({'user_id': user_id})

        finances = self.finance_repository.get_by_filters(filters, pagination)
        finances_schema = FinanceSchema(many=True)

        items = finances.get('items')
        del finances['items']
        balance = finances.get('balance')
        del finances['balance']
        return {
            'items': finances_schema.dump(items),
            'balance': balance,
            'pagination': finances
        }

    def get_by_id(self, id: int) -> Finance:
        self.logger.info('[FinanceService]: Getting finance by id: {id}')
        finance = self.finance_repository.get_by_id(id)

        if not finance:
            raise ValidationError('Finance not found')

        finance_schema = FinanceSchema(partial=True)

        return finance_schema.dump(finance)
