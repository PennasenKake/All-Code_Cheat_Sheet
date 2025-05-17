# src/tests/test_main.py
# Yksikkötestit API:lle

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_greet():
    response = client.get("/api/greet?name=Akash")
    assert response.status_code == 200
    assert response.json() == {"message": "Hei, Akash!"}

def test_create_user():
    user_data = {"name": "Akash", "age": 30}
    response = client.post("/api/create-user", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Käyttäjä Akash lisätty!"}

def test_add_item():
    item_data = {"name": "Notebook", "price": 9.99, "in_stock": true}
    response = client.post("/api/add-item", json=item_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Notebook lisätty!"