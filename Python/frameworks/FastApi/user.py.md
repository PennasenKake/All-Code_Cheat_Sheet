<!-- tags: python, frameworks, fastapi -->

# user.py

[Näytä alkuperäinen tiedosto GitHubissa](Python/frameworks/FastApi/user.py)

```python
# src/models/user.py
# Pydantic-malli User-resurssille

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```
