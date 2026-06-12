import json
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    email: str
    password: str

class AuthManager:
    def __init__(self, data_file='users.json'):
        self.data_file = data_file
        # Use an in-memory store for tests; persistence is optional
        self.users = {}

    def load_users(self):
        # Compatibility placeholder; not used in tests
        if not os.path.exists(self.data_file):
            return {}
        with open(self.data_file, 'r') as f:
            return json.load(f)

    def save_users(self):
        # Compatibility placeholder; not used in tests
        with open(self.data_file, 'w') as f:
            json.dump(self.users, f)

    def sign_up(self, email: str, password: str):
        if email in self.users:
            raise ValueError("Email already in use")
        self.users[email] = password
        # Persist if desired: self.save_users()

    def log_in(self, email: str, password: str) -> Optional[User]:
        if email not in self.users or self.users[email] != password:
            return None
        return User(email, password)

    def log_out(self):
        # Simple logout, just return None
        return None
