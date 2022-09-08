from flask import url_for
from application import app
from flask_testing import TestCase
import pytest


class TestBase(TestCase):
    def create_app(self):
        return app

class TestHomeView(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
