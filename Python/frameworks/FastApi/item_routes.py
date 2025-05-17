# src/routes/item_routes.py
# Reitit Item-resurssille

from fastapi import APIRouter
from models.item import Item

router = APIRouter()

# POST-reitti tuotteen lisäämiselle
@router.post("/add-item")
def add_item(item: Item):
    return {"message": f"{item.name} lisätty!", "item": item}