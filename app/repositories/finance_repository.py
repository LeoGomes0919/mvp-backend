from datetime import datetime

from app.models import Finance
from app.repositories.base_repository import BaseRepository


class FinanceRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Finance)

    def get_by_filters(self, filters: dict, params: dict):
        query = self.session.query(Finance).filter(Finance.user_id == filters.get('user_id'))

        # create balance
        balance = {
            'income': 0,
            'outcome': 0,
            'total': 0
        }

        query_income = query.filter(Finance.finance_type == 'income')
        query_outcome = query.filter(Finance.finance_type == 'outcome')

        balance['income'] = query_income.with_entities(Finance.value).all()
        balance['outcome'] = query_outcome.with_entities(Finance.value).all()

        balance['income'] = sum([item[0] for item in balance['income']])
        balance['outcome'] = sum([item[0] for item in balance['outcome']])
        balance['total'] = balance['income'] - balance['outcome']

        if filters.get('description'):
            query = query.filter(Finance.description.like(f'%{filters.get("description")}%'))

        if filters.get('finance_type'):
            query = query.filter(Finance.finance_type == filters.get('finance_type'))

        total_items = query.count()
        finances = query.offset((params['page'] - 1) * params['per_page']).limit(params['per_page']).all()

        return {
            'page': params['page'],
            'per_page': params['per_page'],
            'total_pages': (total_items + params['per_page'] - 1) // params['per_page'],
            'total_items': total_items,
            'items': finances,
            'balance': balance
        }
