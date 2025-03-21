from typing import Optional
from pydantic import BaseModel, HttpUrl

class ReceitaBase(BaseModel):  # Classe base para campos comuns
    nome: str
    ingredientes: str
    tempo_preparo: str
    modo_preparo: str

class ReceitaCreate(ReceitaBase):  # Para criar uma nova receita (sem ID)
    url_imagem: Optional[HttpUrl] = None  # Adicione isso
    url_video: Optional[HttpUrl] = None  # Adicione isso

class ReceitaUpdate(ReceitaBase):  # Para atualizar uma receita (sem ID, campos opcionais)
    nome: Optional[str] = None
    ingredientes: Optional[str] = None
    tempo_preparo: Optional[str] = None
    modo_preparo: Optional[str] = None
    url_imagem: Optional[HttpUrl] = None
    url_video: Optional[HttpUrl] = None

class Receita(ReceitaBase):  # Para retornar a receita com o ID
    id: int
    url_imagem: Optional[HttpUrl] = None
    url_video: Optional[HttpUrl] = None

    class Config:
        orm_mode = True  # Permite converter objetos SQLAlchemy para Pydantic