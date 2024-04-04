from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_add_an_item_API():
    response = client.get("/items/1234")
    assert(response.status_code == 200)
    assert(response.json() == {
        "item_id": 1234,
        "q": "hello"
    })