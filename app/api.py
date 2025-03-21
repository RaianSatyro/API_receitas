from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/receitas/", response_model=schemas.Receita)
async def criar_receita_api(receita: schemas.ReceitaCreate, db: Session = Depends(get_db)):
    return crud.criar_receita(db=db, receita=receita)

@router.get("/receitas/{receita_id}", response_model=schemas.Receita)
async def ler_receita_api(receita_id: int, db: Session = Depends(get_db)):
    db_receita = crud.ler_receita(db=db, receita_id=receita_id)
    if db_receita is None:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return db_receita

@router.get("/receitas/", response_model=List[schemas.Receita])
async def listar_receitas_api(db: Session = Depends(get_db)):
    return crud.listar_receitas(db=db)

@router.put("/receitas/{receita_id}", response_model=schemas.Receita)
async def atualizar_receita_api(receita_id: int, receita: schemas.ReceitaUpdate, db: Session = Depends(get_db)):
    db_receita = crud.atualizar_receita(db=db, receita_id=receita_id, receita=receita)
    if db_receita is None:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return db_receita

@router.delete("/receitas/{receita_id}", status_code=204) # Retorna 204 No Content em caso de sucesso
async def deletar_receita_api(receita_id: int, db: Session = Depends(get_db)):
    if not crud.deletar_receita(db=db, receita_id=receita_id):
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return None  # FastAPI espera que não haja retorno para status code 204