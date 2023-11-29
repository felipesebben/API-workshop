from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schema import ProdutosSchema
from app.config import SessionLocal, get_db
from app.model import Produto

router = APIRouter()

# Criar rota principal
@router.get("/")  # Request
def ola_mundo():  # Response
    return {"Olá": "Mundo"}


# Criar novo endpoint de lista de produtos
@router.get("/produtos", response_model=List[ProdutosSchema])  # Schema  de resposta
def listar_produtos(db: Session = Depends(get_db)):
    """
    Retorna lista de produtos.
    """
    return db.query(Produto).all()  # = SELECT * FROM produtos


# Criar novo endpoint para produto específico
@router.get(
    "/produtos/{produto_id}", response_model=ProdutosSchema
)  # Schema  de resposta
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    """
    Retorna produto específico.
    """
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


@router.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema, db: Session = Depends(get_db)):
    """
    Adiciona novo produto.
    """
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto


@router.delete("/produtos/{produto_id}", response_model=ProdutosSchema)
async def remover_produto(
    produto_id: int, db: Session = Depends(get_db)
):  # Async para rodar em background
    """
    Remove produto.
    """
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


@router.put("/produtos/{produto_id}", response_model=ProdutosSchema)
def atualizar_produto(
    produto_id: int, produto_data: ProdutosSchema, db: Session = Depends(get_db)
):
    """
    Atualiza produto.
    """
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if db_produto:
        for key, value in produto_data.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit()
        db.refresh(db_produto)
        return db_produto
    else:
        return HTTPException(status_code=404, detail="Produto não encontrado")
