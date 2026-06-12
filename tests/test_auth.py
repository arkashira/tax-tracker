from auth import AuthManager, User

def test_sign_up():
    auth = AuthManager()
    auth.sign_up('test@example.com', 'password')
    assert 'test@example.com' in auth.users

def test_log_in():
    auth = AuthManager()
    auth.sign_up('test@example.com', 'password')
    user = auth.log_in('test@example.com', 'password')
    assert user.email == 'test@example.com'
    assert user.password == 'password'

def test_log_in_failure():
    auth = AuthManager()
    user = auth.log_in('test@example.com', 'password')
    assert user is None

def test_log_out():
    auth = AuthManager()
    result = auth.log_out()
    assert result is None
