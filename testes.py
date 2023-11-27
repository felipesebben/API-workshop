import pytest

from fastapi.testclient import TestClient # Servidor de testes do FastAPI

from main import app

client = TestClient(app)

def teste_ola_mundo():
    """
    Teste para verificar se a rota principal está funcionando.
    """
    response = client.get("/")
    assert response.status_code == 200 # Verifica se o status code é 200
    
    
def teste_ola_mundo_json():
    """
    Teste para verificar se a rota principal está retornando o JSON correto.
    """
    response = client.get("/")
    assert response.json() == {"Olá": "Mundo"}


def teste_listar_produtos_status_code():
    """
    Teste para verificar se a rota de listagem de produtos está funcionando.
    """
    response = client.get("/produtos")
    assert response.status_code == 200 # Verifica se o status code é 200


def test_tamanho_da_lista_de_produtos():
    """
    Teste para verificar se a rota de listagem de produtos está retornando a lista correta.
    """
    response = client.get("/produtos")
    assert len(response.json()) == 3 # Verifica se a lista tem 3 itens