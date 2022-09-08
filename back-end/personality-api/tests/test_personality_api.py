rom flask import url_for
from flask_testing import TestCase
import pytest
from unittest.mock import patch

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app
    
    def test_choice(self):
        element = random.choice(self.a)
        self.assertTrue(element in self.a)

    def test_sample(self):
        for element in random.sample(self.a,b'Anticipative' ):
            self.assertTrue(element in self.a)

class TestViews(TestBase):

    def test_get_character(self):
        response = self.client.get(url_for('personality'))
        self.assertEqual(response.status_code, 200)