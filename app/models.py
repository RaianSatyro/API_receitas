from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class CategoriaDB(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), unique=True, index=True)
    descricao = Column(Text, nullable=True)

    receitas = relationship("ReceitaDB", back_populates="categoria") # Relacionamento

class ReceitaDB(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), index=True)
    ingredientes = Column(Text)
    tempo_de_preparo = Column(String(50))
    modo_preparo = Column(Text)
    url_imagem = Column(String(2048), nullable=True, name="url_imagem")
    url_video = Column(String(2048), nullable=True, name="url_video")
    categoria_id = Column(Integer, ForeignKey("categorias.id")) # Chave estrangeira

    categoria = relationship("CategoriaDB", back_populates="receitas") # Relacionamento