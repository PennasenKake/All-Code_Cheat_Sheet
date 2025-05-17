# src/main.py
# Pääsovellus FastAPI:lle

from fastapi import FastAPI
from routes.basic_routes import router as basic_router
from routes.item_routes import router as item_router

# Luodaan FastAPI-instanssi
app = FastAPI(
    title="FastAPI Esimerkkisovellus",
    description="Yksinkertainen API FastAPI:lla",
    version="1.0.0",
)

# Liitetään reitit
app.include_router(basic_router, prefix="/api")
app.include_router(item_router, prefix="/api")