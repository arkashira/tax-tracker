from unittest import TestCase
from src.profile import ProfileManager
import os

class TestProfileManager(TestCase):
    def setUp(self):
        self.manager = ProfileManager('test_profiles.json')

    def tearDown(self):
        if os.path.exists('test_profiles.json'):
            os.remove('test_profiles.json')

    def test_create_profile(self):
        self.manager.create_profile('test', 'test@example.com', 'password')
        self.assertIn('test', self.manager.profiles)

    def test_update_profile(self):
        self.manager.create_profile('test', 'test@example.com', 'password')
        self.manager.update_profile('test', email='new@example.com')
        self.assertEqual(self.manager.profiles['test']['email'], 'new@example.com')

    def test_delete_profile(self):
        self.manager.create_profile('test', 'test@example.com', 'password')
        self.manager.delete_profile('test')
        self.assertNotIn('test', self.manager.profiles)

    def test_change_password(self):
        self.manager.create_profile('test', 'test@example.com', 'password')
        self.manager.update_profile('test', password='newpassword')
        self.assertEqual(self.manager.profiles['test']['password'], 'newpassword')
