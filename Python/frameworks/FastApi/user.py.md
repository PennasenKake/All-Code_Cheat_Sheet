<!-- tags: python, frameworks, fastapi -->

# user.py

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/Python/frameworks/FastApi/user.py)

```python
# src/models/user.py
# Pydantic-malli User-resurssille

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```
