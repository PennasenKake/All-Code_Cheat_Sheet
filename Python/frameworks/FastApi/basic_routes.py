# src/routes/basic_routes.py
# Perusreitit (Hello World, GET, POST)

from fastapi import APIRouter
from models.user import User

router = APIRouter()

# Hello World -reitti
@router.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# GET-reitti tervehdykselle
@router.get("/greet")
def greet(name: str):
    return {"message": f"Hei, {name}!"}

# POST-reitti käyttäjän luomiselle
@router.post("/create-user")
def create_user(user: User):
    return {"message": f"Käyttäjä {user.name} lisätty!"}