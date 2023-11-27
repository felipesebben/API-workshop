from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProdutosSchema(BaseModel):
    """
    Modelo de dados para produtos.
    """
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat