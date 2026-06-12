import pytest
from user_profile import UserManager, User


def test_update_profile():
    manager = UserManager()
    user = manager.create_user("123", "Alice", "alice@example.com", "oldpass")
    
    assert manager.update_profile("123", name="Alice Smith", email="new@example.com")
    updated = manager.get_user("123")
    assert updated.name == "Alice Smith"
    assert updated.email == "new@example.com"


def test_change_password():
    manager = UserManager()
    user = manager.create_user("456", "Bob", "bob@example.com", "oldpass")
    
    assert manager.change_password("456", "oldpass", "newpass")
    assert not manager.change_password("456", "wrongpass", "anotherpass")
    assert manager.get_user("456").password == "newpass"


def test_delete_account():
    manager = UserManager()
    manager.create_user("789", "Charlie", "charlie@example.com", "pass123")
    
    assert manager.delete_account("789")
    assert manager.get_user("789") is None
    assert not manager.delete_account("nonexistent")


def test_create_user():
    manager = UserManager()
    user = manager.create_user("101", "Dave", "dave@example.com", "pass")
    assert user.user_id == "101"
    assert manager.get_user("101") is not None
    
    with pytest.raises(ValueError):
        manager.create_user("101", "Dave", "dave@example.com", "pass")
