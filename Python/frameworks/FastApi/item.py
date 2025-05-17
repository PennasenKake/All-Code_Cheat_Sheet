# src/models/item.py
# Pydantic-malli Item-resurssille

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool