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
