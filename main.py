from fastapi import FastAPI
from app.api import router as api_router
from fastapi.middleware.cors import CORSMiddleware
import logging
import os
from app.database import create_database
# Configuração do logging
logging.basicConfig(level=logging.INFO)

logging.info("API Iniciando...")

app = FastAPI()
logging.info("Instância FastAPI criada.")

# Configuração do CORS (use variáveis de ambiente em produção)
ALLOWED_ORIGINS_STR = os.getenv("ALLOWED_ORIGINS", "")
ALLOWED_ORIGINS = ALLOWED_ORIGINS_STR.split(",") if ALLOWED_ORIGINS_STR else ["*"]  # NÃO USE "*" EM PRODUÇÃO!

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclua o router da API
try:
    app.include_router(api_router)
    logging.info("Router da API incluído com sucesso.")
except Exception as e:
    logging.error(f"Erro ao incluir o router da API: {e}")

@app.get("/")
async def read_root():
    logging.info("Função root chamada.")
    return {"message": "Bem-vindo à API de Receitas!"}

# Inicialização do banco de dados
try:
    create_database()
    logging.info("Banco de dados inicializado.")
except Exception as e:
    logging.error(f"Erro ao inicializar o banco de dados: {e}")