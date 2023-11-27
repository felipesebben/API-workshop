from fastapi import FastAPI
from app.schema import ProdutosSchema
from app.data import Produtos

# Criar instância do FastAPI
app = FastAPI()
# Criar instância da lista de produtos
lista_de_produtos = Produtos()

# Criar rota principal
@app.get("/")   # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo"}

# Criar novo endpoint de lista de produtos
@app.get("/produtos", response_model=list[ProdutosSchema]) # Schema  de resposta
def listar_produtos():
    """
    Retorna lista de produtos.
    """
    return lista_de_produtos.listar_produtos()

# Criar novo endpoint para produto específico
@app.get("/produtos/{id}", response_model=ProdutosSchema) # Schema  de resposta
def buscar_produto(id: int):
    """
    Retorna produto específico.
    """
    return lista_de_produtos.buscar_produto(id)

@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
    """
    Adiciona novo produto.
    """
    return lista_de_produtos.adicionar_produtos(produto.model_dump())