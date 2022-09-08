from flask import url_for
from flask_testing import TestCase
import pytest
from unittest.mock import patch
import random

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestViews(TestBase):
    def test_get_character(self):
        with patch('random.choice') as r:
            r.return_value = "Anticipative", "Brave", "Curious"
            response = self.client.get(url_for('personality'))
            self.assertEqual(response.status_code, 200)
