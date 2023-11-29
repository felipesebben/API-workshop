from enum import Enum
from pydantic import BaseModel, PositiveFloat
from typing import Optional


class ProdutosSchema(BaseModel):
    """
    Modelo de dados para produtos.
    """

    id: Optional[int] = None
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat

    class Config:
        orm_mode = True
        # Habilita o modo ORM para que o Pydantic possa ler os dados do SQLAlchemy
