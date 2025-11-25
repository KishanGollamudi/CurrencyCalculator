from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

client = TestClient(app)


def test_list_currencies():
    resp = client.get("/api/currencies")
    assert resp.status_code == 200
    data = resp.json()
    assert "currencies" in data
    assert "INR" in data["currencies"]


def test_convert_currency():
    payload = {
        "from_currency": "INR",
        "to_currency": "USD",
        "amount": 1000
    }
    resp = client.post("/api/convert", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["from_currency"] == "INR"
    assert data["to_currency"] == "USD"
    assert data["converted_amount"] > 0

