<!-- tags: python, frameworks, fastapi -->

# item.py

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/Python/frameworks/FastApi/item.py)

```python
# src/models/item.py
# Pydantic-malli Item-resurssille

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool
```
