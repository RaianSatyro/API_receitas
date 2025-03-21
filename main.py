from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI()
app.include_router(api_router)

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API de Receitas!"}