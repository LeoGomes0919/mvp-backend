import datetime

from flask_jwt_extended import create_access_token, create_refresh_token

from app.models import User
from app.repositories import user_repository
from app.utils import ValidationError, logger


class AuthService:
    def __init__(self):
        self.logger = logger
        self.user_repository = user_repository
        self.user = User()

    def auth_user(self, data: dict) -> User:
        self.logger.info(f'[AuthService]: Authenticating user: {data["email"]}')

        user = self.user_repository.get_by_email(data['email'])
        if not user:
            self.logger.error(f'[AuthService]: Incorrect username or password: {data["email"]}')
            raise ValidationError('Incorrect username or password', 400)

        # validate password
        matched_password = self.user.compare_hash(data['password'], user.password)

        if not matched_password:
            self.logger.error(f'[AuthService]: Incorrect username or password: {data["email"]}')
            raise ValidationError('Incorrect username or password', 400)

        access_token = create_access_token(
            identity={'user_id': user.id, 'email': user.email}, expires_delta=datetime.timedelta(days=1))
        refresh_token = create_refresh_token(identity=user.id)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
