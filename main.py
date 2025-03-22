from fastapi import FastAPI
from app.api import router as api_router
import logging


logging.basicConfig(level=logging.INFO)
logging.info("API Iniciando...")

app = FastAPI()
app.include_router(api_router)

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API de Receitas!"}