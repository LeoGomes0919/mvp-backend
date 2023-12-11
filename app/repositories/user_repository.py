from app.models import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(User)

    def get_by_email(self, email: str) -> User:
        result = self.session.query(User).filter(User.email == email).first()
        self.session.close()
        return result
