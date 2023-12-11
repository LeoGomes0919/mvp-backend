from datetime import datetime

from app.models import Finance
from app.repositories.base_repository import BaseRepository


class FinanceRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Finance)

    def get_by_filters(self, filters: dict, params: dict):
        query = self.session.query(Finance)

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
            'items': finances
        }
