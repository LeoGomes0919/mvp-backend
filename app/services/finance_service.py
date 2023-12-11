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

    def create(self, data: dict) -> Finance:
        self.logger.info('[FinanceService]: Creating finance: {data}')
        category = self.category_repository.get_by_id(data.get('category_id'))

        sub = get_jwt_identity()
        user_id = sub.get('user_id')

        if not user_id or not category:
            raise ValidationError('Error on create finance')

        now = datetime.now()
        data.update({'date': now, 'user_id': user_id})

        self.finance_repository.create(data)

    def update(self, id: str, data: dict) -> None:
        self.logger.info('[FinanceService]: Updating finance: {id}')
        finance = self.finance_repository.get_by_id(id)

        if not finance:
            raise ValidationError('Error on update finance')

        category = self.category_repository.get_by_id(data.get('category_id'))

        if not category:
            raise ValidationError('Error on update finance')

        data.update({'date': finance.date, 'id': id})

        self.finance_repository.update(data)

    def delete(self, id: str) -> None:
        self.logger.info('[FinanceService]: Deleting finance: {id}')
        finance = self.finance_repository.get_by_id(id)

        if not finance:
            raise ValidationError('Error on delete finance')

        return self.finance_repository.delete(finance)

    def get_by_filters(self, filters: dict, params: dict):
        self.logger.info('[FinanceService]: Getting all finances')

        if filters.get('finance_type'):
            if filters.get('finance_type') == 'entrada':
                filters['finance_type'] = 'income'
            else:
                filters['finance_type'] = 'outcome'

        finances = self.finance_repository.get_by_filters(filters, params)
        finances_schema = FinanceSchema(many=True)

        items = finances.get('items')
        del finances['items']

        return {
            'items': finances_schema.dump(items),
            'pagination': finances
        }

    def get_by_id(self, id: int) -> Finance:
        self.logger.info('[FinanceService]: Getting finance by id: {id}')
        finance = self.finance_repository.get_by_id(id)

        if not finance:
            raise ValidationError('Finance not found')

        finance_schema = FinanceSchema(partial=True)

        return finance_schema.dump(finance)
