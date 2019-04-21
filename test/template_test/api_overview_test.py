"""Tests for the rendering of the API overview page.
"""

def test_api_overview_status_and_content_type(test_client):
    """Test rendering of the API overview page.

    Args:
        test_client (FlaskClient): The test client.
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "text/html; charset=utf-8"


def test_api_overview_v1(test_client):
    """Test rendering of the API v1.

    Args:
        test_client (FlaskClient): The test client.
    """
    response = test_client.get("/")
    assert "<a href=\"/api/v1\">ingredients_api_v1</a>" in str(response.data)
