from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):

    def test_get_character(self):
        response = self.client.post(url_for('character'), json={"Colour": "Red", "Personality":"Anticipative""Brave""Curious"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Character', response.data)