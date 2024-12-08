import pytest
from fastapi.testclient import TestClient
from mongomock import MongoClient

from src.app import build_app
from src.common.db import MongoDB


@pytest.fixture
def mock_mongodb(monkeypatch):
    def mock_init(self):
        self.db_config = {
            'dsn': 'mongodb://testdb',
            'templates': [
                {
                    'name': 'Contact form',
                    'fields': {
                        'email': 'email',
                        'phone': 'phone'
                    }
                },
                {
                    'name': 'Registration',
                    'fields': {
                        'user_email': 'email',
                        'birth_date': 'date',
                        'phone_number': 'phone'
                    }
                }
            ]
        }
        self.conn = MongoClient()
        self.db = self.conn['forms_db']
        self.form_templates = self.db['form_templates']
        self._init_templates()

    monkeypatch.setattr(MongoDB, "__init__", mock_init)
    return MongoDB()


@pytest.fixture
def test_app(mock_mongodb):
    app = build_app()
    return app


@pytest.fixture
def test_client(test_app):
    return TestClient(test_app)
