import dataclasses
from typing import Optional, Dict


@dataclasses.dataclass
class User:
    user_id: str
    name: str
    email: str
    password: str


class UserManager:
    def __init__(self):
        self._users: Dict[str, User] = {}

    def get_user(self, user_id: str) -> Optional[User]:
        return self._users.get(user_id)

    def update_profile(self, user_id: str, name: Optional[str] = None, email: Optional[str] = None) -> bool:
        user = self._users.get(user_id)
        if not user:
            return False
            
        if name:
            user.name = name
        if email:
            user.email = email
        return True

    def change_password(self, user_id: str, current_password: str, new_password: str) -> bool:
        user = self._users.get(user_id)
        if not user or user.password != current_password:
            return False
            
        user.password = new_password
        return True

    def delete_account(self, user_id: str) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False

    def create_user(self, user_id: str, name: str, email: str, password: str) -> User:
        if user_id in self._users:
            raise ValueError("User already exists")
        user = User(user_id, name, email, password)
        self._users[user_id] = user
        return user
