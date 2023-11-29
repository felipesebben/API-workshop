import pytest
from fastapi.testclient import TestClient  # Servidor de testes do FastAPI
from app.main import app

from pydantic import ValidationError


def teste_ola_mundo():
    """
    Teste para verificar se a rota principal está funcionando.
    """
    response = TestClient(app).get("/")
    assert response.status_code == 200  # Verifica se o status code é 200


def teste_ola_mundo_json():
    """
    Teste para verificar se a rota principal está retornando o JSON correto.
    """
    response = TestClient(app).get("/")
    assert response.json() == {"Olá": "Mundo"}


@pytest.fixture
def test_client():
    """
    Cria uma instância de TestClient que pode ser usada em testes.
    O TestClient é utilizado para simular requisicoes à API FastAPI.
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture
def produto_id(test_client):
    """
    Fixture que cria um produto na API e retorna o ID desse produto.
    Utilizado para testar operações que necessitem de um produto existente.
    """
    produto_data = {
        "titulo": "Produto Teste",
        "descricao": "Descrição do produto teste",
        "preco": 100.00,
    }
    response = test_client.post("/produtos", json=produto_data)
    assert response.status_code == 200
    return response.json()["id"]


def test_listar_produtos(test_client):
    """
    Testa se a rota GET `/produtos` retorna uma lista de produtos e um status code 200.
    Verifica se a resposta é uma lista, indicando uma listagem bem-sucedida.
    """
    response = test_client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_inserir_produto(test_client):
    """
    Testa a criação de um produto mediante a rota POST `/produtos`.
    Verifica se o produto é criado com sucesso e se os dados retornados são corretos.
    """
    produto_data = {
        "titulo": "Produto Teste",
        "descricao": "Descrição do produto teste",
        "preco": 100.00,
    }
    response = test_client.post("/produtos", json=produto_data)
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == produto_data["titulo"]
    assert data["descricao"] == produto_data["descricao"]
    assert data["preco"] == produto_data["preco"]


def test_obter_produto(test_client, produto_id):
    """
    Testa a obtenção de um produto mediante a rota GET `/produtos/{produto_id}`.
    Verifica se o produto é retornado com sucesso e se os dados retornados são corretos.
    """
    response = test_client.get(f"/produtos/{produto_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == produto_id
    assert "titulo" in data


def test_atualizar_produto(test_client, produto_id):
    """
    Testa a atualização de um produto existente pela rota PUT `/produtos/{produto_id}`.
    Verifica se o produto é atualizado com sucesso e se os dados retornados são corretos.
    """
    novo_dado = {
        "titulo": "Produto Atualizado",
        "descricao": "Descrição do produto atualizado",
        "preco": 200.00,
    }
    response = test_client.put(f"/produtos/{produto_id}", json=novo_dado)
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == novo_dado["titulo"]


def test_remover_produto(test_client, produto_id):
    """
    Testa a remoção de um produto pela rota DELETE `/produtos/{produto_id}`.
    Verifica se o produto é removido com sucesso e se o mesmo não é mais encontrado após a remoção.
    """
    response = test_client.delete(f"/produtos/{produto_id}")
    assert response.status_code == 200
    response = test_client.get(f"/produtos/{produto_id}")
    assert response.status_code == 404


from app.schema import ProdutosSchema


def test_modelo_produto_valido():
    """
    Testa se o modelo de dados de produtos é válido.
    """
    produto = ProdutosSchema(titulo="Teste", descricao="Descricao Teste", preco=10.0)
    assert produto.titulo == "Teste"
    assert produto.preco == 10.0


def test_modelo_produto_invalido():
    """
    Testa se o modelo de dados de produtos é inválido.
    """
    with pytest.raises(ValidationError):
        ProdutosSchema(titulo="", preco=-10.0)
