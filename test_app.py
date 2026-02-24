"""
Test suite for Flask Hello World Web Application

Tests the root endpoint and Flask application functionality.
"""

import pytest
from app import app


@pytest.fixture
def client():
    """
    Create a test client for the Flask application.
    
    Returns:
        Flask test client
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_world_endpoint(client):
    """
    Test that the root endpoint returns 'Hello, World!'.
    
    This is the main functionality test for the Hello World app.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!'


def test_hello_world_status_code(client):
    """
    Test that the root endpoint returns HTTP 200 status code.
    """
    response = client.get('/')
    assert response.status_code == 200


def test_hello_world_content_type(client):
    """
    Test that the response content type is text/html.
    """
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'


def test_app_exists():
    """
    Test that the Flask app instance exists and is properly configured.
    """
    assert app is not None
    assert app.name == 'app'