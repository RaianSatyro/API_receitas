from sqlalchemy import Column, Integer, String, Text
from .database import Base

class ReceitaDB(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    ingredientes = Column(Text)
    tempo_preparo = Column(String)
    modo_preparo = Column(Text)
    url_imagem = Column(String, nullable=True)
    url_video = Column(String, nullable=True)