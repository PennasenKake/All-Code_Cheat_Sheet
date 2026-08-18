<!-- tags: python, frameworks, fastapi -->

# item_routes.py

[Näytä alkuperäinen tiedosto GitHubissa](Python/frameworks/FastApi/item_routes.py)

```python
# src/routes/item_routes.py
# Reitit Item-resurssille

from fastapi import APIRouter
from models.item import Item

router = APIRouter()

# POST-reitti tuotteen lisäämiselle
@router.post("/add-item")
def add_item(item: Item):
    return {"message": f"{item.name} lisätty!", "item": item}
```
