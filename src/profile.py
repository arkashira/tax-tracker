import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Profile:
    username: str
    email: str
    password: str

class ProfileManager:
    def __init__(self, filename: str = 'profiles.json'):
        self.filename = filename
        self.profiles = self.load_profiles()

    def load_profiles(self) -> dict:
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_profiles(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump(self.profiles, f)

    def create_profile(self, username: str, email: str, password: str) -> None:
        if username in self.profiles:
            raise ValueError("Username already exists")
        self.profiles[username] = {
            'email': email,
            'password': password
        }
        self.save_profiles()

    def update_profile(self, username: str, email: Optional[str] = None, password: Optional[str] = None) -> None:
        if username not in self.profiles:
            raise ValueError("Username does not exist")
        if email:
            self.profiles[username]['email'] = email
        if password:
            self.profiles[username]['password'] = password
        self.save_profiles()

    def delete_profile(self, username: str) -> None:
        if username not in self.profiles:
            raise ValueError("Username does not exist")
        del self.profiles[username]
        self.save_profiles()
