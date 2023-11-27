from typing import List, Dict

class Produtos:
# Criar lista de produtos
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


    def listar_produtos(self):
        """
        Retorna lista de produtos.
        """
        return self.produtos
    

    def buscar_produto(self, id):
        """
        Retorna produto específico.
        """
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404,
                "Mensagem": "Produto não encontrado."}


    def adicionar_produtos(self, produto):
        """
        Adiciona novo produto.
        """
        self.produtos.append(produto)
        return produto