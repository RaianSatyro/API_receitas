from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
import logging

from . import crud, models, schemas
from .database import get_db

logging.info("API Router iniciando...")

router = APIRouter()

@router.post("/receitas/", response_model=schemas.Receita)
async def criar_receita_api(receita: schemas.ReceitaCreate, db: Session = Depends(get_db)):
    logging.info(f"Rota POST /receitas/ chamada com receita: {receita}")
    try:
        return crud.criar_receita(db=db, receita=receita)
    except Exception as e:
        logging.error(f"Erro ao criar receita: {e}")
        raise HTTPException(status_code=500, detail="Erro ao criar receita")

@router.get("/receitas/{receita_id}", response_model=schemas.Receita)
async def ler_receita_api(receita_id: int, db: Session = Depends(get_db)):
    logging.info(f"Rota GET /receitas/{receita_id} chamada.")
    try:
        db_receita = crud.ler_receita(db=db, receita_id=receita_id)
        if db_receita is None:
            raise HTTPException(status_code=404, detail="Receita não encontrada")
        return db_receita
    except Exception as e:
        logging.error(f"Erro ao ler receita: {e}")
        raise HTTPException(status_code=500, detail="Erro ao ler receita")

@router.get("/receitas/", response_model=List[schemas.Receita])
async def listar_receitas_api(categoria_id: Optional[int] = None, db: Session = Depends(get_db)):
    logging.info(f"Rota GET /receitas/ (listar todas) chamada com categoria_id: {categoria_id}")
    try:
        return crud.listar_receitas(db=db, categoria_id=categoria_id)
    except Exception as e:
        logging.error(f"Erro ao listar receitas: {e}")
        raise HTTPException(status_code=500, detail="Erro ao listar receitas")

@router.put("/receitas/{receita_id}", response_model=schemas.Receita)
async def atualizar_receita_api(receita_id: int, receita: schemas.ReceitaUpdate, db: Session = Depends(get_db)):
    logging.info(f"Rota PUT /receitas/{receita_id} chamada com receita: {receita}")
    try:
        db_receita = crud.atualizar_receita(db=db, receita_id=receita_id, receita=receita)
        return db_receita
    except HTTPException as e:
        raise e # Deixar o crud tratar o erro 404
    except Exception as e:
        logging.error(f"Erro ao atualizar receita: {e}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar receita")

@router.delete("/receitas/{receita_id}", status_code=204) # Retorna 204 No Content em caso de sucesso
async def deletar_receita_api(receita_id: int, db: Session = Depends(get_db)):
    logging.info(f"Rota DELETE /receitas/{receita_id} chamada.")
    try:
        crud.deletar_receita(db=db, receita_id=receita_id)
        return None  # FastAPI espera que não haja retorno para status code 204
    except HTTPException as e:
        raise e # Deixar o crud tratar o erro 404
    except Exception as e:
        logging.error(f"Erro ao deletar receita: {e}")
        raise HTTPException(status_code=500, detail="Erro ao deletar receita")

logging.info("API Router finalizado.")