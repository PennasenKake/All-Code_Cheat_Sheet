<!-- tags: python -->

# async_await.py

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/Python/perusteet/async_await.py)

```python
# async_await.py
# Asynkroninen koodi Pythonissa (Python 3.7+)

import asyncio

async def odota_sekunti():
    print("Odotetaan 1 sekunti...")
    await asyncio.sleep(1)
    print("Valmis!")

async def main():
    await odota_sekunti()

asyncio.run(main())
```
