from pydantic import BaseModel


class SuccessCreatedResponseSchema(BaseModel):
    data: dict = None
    message: str = 'Entity created successfully'
    status: str = 'success'


class SuccessDeletedResponseSchema(BaseModel):
    data: dict = None
    message: str = 'Entity deleted successfully'
    status: str = 'success'


class SuccessUpdatedResponseSchema(BaseModel):
    data: dict = None
    message: str = 'Entity updated successfully'
    status: str = 'success'


class SuccessLoginResponseSchema(BaseModel):
    data: dict = {
        'access_token': 'access_token',
        'refresh_token': 'refresh_token',
    }
    message: str = 'User authenticated successfully'
    status: str = 'success'


class ProfileRepsonseSchema(BaseModel):
    data: dict = {
        'id': 'uuid',
        'email': 'jondoe@gmail.com',
        'name': 'Jon Doe',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
    }
    message: str = 'User found successfully'
    status: str = 'success'


class CategoriesRepsonseSchema(BaseModel):
    items: list = [
        {
            'id': 'uuid',
            'name': 'Category 1',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
        },
        {
            'id': 'uuid',
            'name': 'Category 2',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
        },
    ]
    message: str = 'Categories found successfully'
    status: str = 'success'


class FinanceResponseSchema(BaseModel):
    data: dict = {
        'category': {
            'id': 'uuid',
            'name': 'Category 1',
        },
        'id': 'uuid',
        'description': 'description',
        'value': 1000,
        'finance_type': 'income',
        'date': '2023-01-01 00:00:00',
        'created_at': '2023-01-01 00:00:00',
        'updated_at': '2023-01-01 00:00:00',
    }
    message: str = 'Finance found successfully'
    status: str = 'success'


class FinanceListResponseSchema(BaseModel):
    data: dict = {
        'items':  [
            {
                'category': {
                    'id': 'uuid',
                    'name': 'Category 1',
                },
                'id': 'uuid',
                'description': 'description',
                'value': 1000,
                'finance_type': 'income',
                'date': '2023-01-01 00:00:00',
                'created_at': '2023-01-01 00:00:00',
                'updated_at': '2023-01-01 00:00:00',
            },
            {
                'category': {
                    'id': 'uuid',
                    'name': 'Category 2',
                },
                'id': 'uuid',
                'description': 'description',
                'value': 1000,
                'finance_type': 'income',
                'date': '2023-01-01 00:00:00',
                'created_at': '2023-01-01 00:00:00',
                'updated_at': '2023-01-01 00:00:00',
            },
        ],
        'pagination': {
            'page': 1,
            'per_page': 10,
        }
    }
    message: str = 'Finances found successfully'
    status: str = 'success'


class FinanceNotFoundResponseSchema(BaseModel):
    data: str = 'Finance not found'
    message: str = 'Invalid data provided'
    status: str = 'failure'


class ErrorResponseSchema(BaseModel):
    data: str = 'any error message'
    message: str = 'Something went wrong'
    status: str = 'failure'


class ErrorFieldResponseSchema(BaseModel):
    data: dict = {
        "field": "The field is required",
    }
    message: str = 'Invalid data provided'
    status: str = 'failure'


class ErrorLoginResponseSchema(BaseModel):
    data: str = 'Incorrect username or password'
    message: str = 'Invalid data provided'
    status: str = 'failure'


class ErrorUnauthorizedResponseSchema(BaseModel):
    data: str = 'Missing Authorization Header'
    message: str = 'Invalid data provided'
    status: str = 'failure'
