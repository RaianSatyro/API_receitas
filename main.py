from fastapi import FastAPI
from app.api import router as api_router
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)

logging.info("API Iniciando...")

app = FastAPI()
logging.info("Instância FastAPI criada.")

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

# Adicione este bloco try...except para capturar erros na inicialização
try:
    # Seu código para inicializar o banco de dados (se houver)
    # Exemplo:
    # from app.database import engine, Base
    # Base.metadata.create_all(bind=engine)
    logging.info("Banco de dados inicializado (se aplicável).")
except Exception as e:
    logging.error(f"Erro ao inicializar o banco de dados: {e}")