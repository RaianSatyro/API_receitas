from sqlalchemy.orm import Session
from . import models, schemas

def criar_receita(db: Session, receita: schemas.ReceitaCreate):
    """
    Cria uma nova receita no banco de dados.
    """
    db_receita = models.ReceitaDB(  # Use ReceitaDB (ou o nome correto da sua classe)
        nome=receita.nome,
        ingredientes=receita.ingredientes,
        tempo_preparo=receita.tempo_preparo,
        modo_preparo=receita.modo_preparo,
        url_imagem=str(receita.url_imagem) if receita.url_imagem else None,
        url_video=str(receita.url_video) if receita.url_video else None
    )
    db.add(db_receita)
    db.commit()
    db.refresh(db_receita)
    return db_receita 

def ler_receita(db: Session, receita_id: int):
    return db.query(models.ReceitaDB).filter(models.ReceitaDB.id == receita_id).first()

def listar_receitas(db: Session):
    return db.query(models.ReceitaDB).all()

# Função para atualizar uma receita
def atualizar_receita(db: Session, receita_id: int, receita: schemas.ReceitaUpdate):
    db_receita = db.query(models.ReceitaDB).filter(models.ReceitaDB.id == receita_id).first()
    if db_receita is None:
        return None  # Receita não encontrada
    for var, value in vars(receita).items():
        if value is not None:
            setattr(db_receita, var, value)  # Atualiza os campos que foram fornecidos
    db.commit()
    db.refresh(db_receita)
    return db_receita

# Função para deletar uma receita
def deletar_receita(db: Session, receita_id: int):
    db_receita = db.query(models.ReceitaDB).filter(models.ReceitaDB.id == receita_id).first()
    if db_receita is None:
        return False  # Receita não encontrada
    db.delete(db_receita)
    db.commit()
    return True