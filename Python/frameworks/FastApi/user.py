# src/models/user.py
# Pydantic-malli User-resurssille

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int