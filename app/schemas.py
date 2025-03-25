from typing import Optional, List
from pydantic import BaseModel, HttpUrl, validator

# Schemas para Categoria
class CategoriaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    nome: Optional[str] = None
    descricao: Optional[str] = None

class Categoria(CategoriaBase):
    id: int

    class Config:
        orm_mode = True

# Modifique os schemas de Receita para incluir a categoria
class ReceitaBase(BaseModel):
    nome: str
    ingredientes: str
    tempo_de_preparo: str
    modo_preparo: str
    categoria_id: int  # Adicione a categoria_id

class ReceitaCreate(BaseModel):
    nome: str
    ingredientes: Optional[str] = None
    tempo_de_preparo: str
    modo_preparo: Optional[str] = None
    url_imagem: Optional[HttpUrl] = None
    url_video: Optional[HttpUrl] = None
    categoria_id: int # Adicione a categoria_id

    @validator('url_imagem', 'url_video')
    def validate_url_scheme(cls, value):
        if value and value.scheme not in ('http', 'https'):
            raise ValueError('O URL deve usar o esquema HTTP ou HTTPS')
        return value

class ReceitaUpdate(BaseModel):
    nome: Optional[str] = None
    ingredientes: Optional[str] = None
    tempo_de_preparo: Optional[str] = None
    modo_preparo: Optional[str] = None
    url_imagem: Optional[HttpUrl] = None
    url_video: Optional[HttpUrl] = None
    categoria_id: Optional[int] = None  # Adicione a categoria_id

class Receita(ReceitaBase):
    id: int
    url_imagem: Optional[HttpUrl] = None
    url_video: Optional[HttpUrl] = None
    categoria: Optional[Categoria] = None # Inclui a categoria completa no retorno

    class Config:
        orm_mode = True