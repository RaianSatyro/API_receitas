from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update
from typing import Optional
from . import models, schemas

# CRUD para Categorias
def criar_categoria(db: Session, categoria: schemas.CategoriaCreate):
    db_categoria = models.CategoriaDB(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def ler_categoria(db: Session, categoria_id: int):
    return db.query(models.CategoriaDB).filter(models.CategoriaDB.id == categoria_id).first()

def listar_categorias(db: Session):
    return db.query(models.CategoriaDB).all()

def atualizar_categoria(db: Session, categoria_id: int, categoria: schemas.CategoriaUpdate):
    db_categoria = db.query(models.CategoriaDB).filter(models.CategoriaDB.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    update_data = categoria.dict(exclude_unset=True)
    db.execute(update(models.CategoriaDB).where(models.CategoriaDB.id == categoria_id).values(update_data))
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def deletar_categoria(db: Session, categoria_id: int):
    db_categoria = db.query(models.CategoriaDB).filter(models.CategoriaDB.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    db.delete(db_categoria)
    db.commit()
    return True

# Modifique a função criar_receita para usar a categoria_id
def criar_receita(db: Session, receita: schemas.ReceitaCreate):
    # Converte HttpUrl para string antes de passar para o banco de dados
    receita_dict = receita.dict()
    receita_dict['url_imagem'] = str(receita.url_imagem) if receita.url_imagem else None
    receita_dict['url_video'] = str(receita.url_video) if receita.url_video else None
    db_receita = models.ReceitaDB(**receita_dict)
    db.add(db_receita)
    db.commit()
    db.refresh(db_receita)
    return db_receita

# Modifique a função ler_receita para retornar a categoria
def ler_receita(db: Session, receita_id: int):
    return db.query(models.ReceitaDB).filter(models.ReceitaDB.id == receita_id).first()

def listar_receitas(db: Session, categoria_id: Optional[int] = None):
    query = db.query(models.ReceitaDB)
    if categoria_id is not None:
        query = query.filter(models.ReceitaDB.categoria_id == categoria_id)
    return query.all()

def atualizar_receita(db: Session, receita_id: int, receita: schemas.ReceitaUpdate):
    db_receita = db.query(models.ReceitaDB).filter(models.ReceitaDB.id == receita_id).first()
    if db_receita is None:
        raise HTTPException(status_code=404, detail="Receita não encontrada")

    update_data = receita.dict(exclude_unset=True)

    db.execute(update(models.ReceitaDB).where(models.ReceitaDB.id == receita_id).values(update_data))
    db.commit()
    db.refresh(db_receita)
    return db_receita

def deletar_receita(db: Session, receita_id: int):
    db_receita = db.query(models.ReceitaDB).filter(models.ReceitaDB.id == receita_id).first()
    if db_receita is None:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    db.delete(db_receita)
    db.commit()
    return True