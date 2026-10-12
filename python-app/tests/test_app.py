import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello from GitHub Actions" in resp.data


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_api_info(client):
    data = client.get("/api/info").get_json()
    assert {"version", "environment", "hostname", "commit"} <= data.keys()
