from fastapi import FastAPI
from typing import Dict, List


# Criar instância do FastAPI
app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone", 
        "descricao": "Um telefone que é inteligente",
        "preco": 1500.00,

    },
    {
        "id": 2, 
        "nome": "Notebook",
        "descricao": "Um computador que cabe na sua mochila",
        "preco": 3500.00,
    },
    {
        "id": 3, 
        "nome": "Smartwatch",
        "descricao": "Um relógio inteligente",
        "preco": 800.00,
    },
]

# Criar rota principal
@app.get("/")   # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo"}

# Criar novo endpoint de lista de produtos
@app.get("/produtos")
def listar_produtos():
    """
    Retorna lista de produtos.
    """
    return produtos

# Criar novo endpoint para produto específico
@app.get("/produtos/{id}")
def buscar_produto(id: int):
    """
    Retorna produto específico.
    """
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return {"Status": 404,
            "Mensagem": "Produto não encontrado."}