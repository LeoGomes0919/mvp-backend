from flask_jwt_extended import get_jwt_identity

from app.models import User, UserSchema
from app.repositories import user_repository
from app.utils import ValidationError, logger


class UserService:
    def __init__(self):
        self.logger = logger
        self.user_repository = user_repository
        self.user = User()

    def create(self, data: dict) -> None:
        self.logger.info(f'[UserService]: Creating a new user: {data["name"]}')

        user_exists = self.user_repository.get_by_email(data['email'])

        if user_exists:
            self.logger.error(f'[UserService]: User already exists: {data["email"]}')
            raise ValidationError('User already exists', 400)

        # hash password
        data['password'] = self.user.generate_hash(data['password'])
        user = self.user_repository.create(data)

        return user

    def profile(self) -> User:
        sub = get_jwt_identity()
        user_id = sub.get('user_id')
        self.logger.info(f'[UserService]: Getting user: {user_id}')

        user = self.user_repository.get_by_id(user_id)

        if not user:
            self.logger.error(f'[UserService]: User not found: {user_id}')
            raise ValidationError('User not found', 400)

        user_schema = UserSchema(partial=True)

        return user_schema.dump(user)
