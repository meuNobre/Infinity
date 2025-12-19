from funcoes import Produto, Venda

def menu():
    while True:
        escolha = input("""
Escolha uma opção:
1 - Cadastrar Produto
2 - Listar Produtos
3 - Atualizar Produto
4 - Excluir Produto
5 - Registrar Venda
0 - Sair
""")
        if escolha == "1":
            nome = input("Nome do produto: ")
            descricao = input("Descrição: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            produto = Produto(None, nome, descricao, quantidade, preco)
            print(produto.salvar())

        elif escolha == "2":
            produtos = Produto.listar()
            for p in produtos:
                print(f"ID: {p['id']}, Nome: {p['nome']}, Desc: {p['descricao']}, Quant: {p['quantidade']}, Preço: {p['preco']}")
            print(f"Total de produtos: {len(produtos)}")

        elif escolha == "3":
            id = int(input("ID do produto: "))
            quantidade = input("Nova quantidade (Enter para manter): ")
            preco = input("Novo preço (Enter para manter): ")
            quantidade = int(quantidade) if quantidade else None
            preco = float(preco) if preco else None
            print(Produto.atualizar(id, quantidade, preco))

        elif escolha == "4":
            id = int(input("ID do produto para excluir: "))
            print(Produto.excluir(id))

        elif escolha == "5":
            produto_id = int(input("ID do produto vendido: "))
            quantidade = int(input("Quantidade vendida: "))
            venda = Venda(produto_id, quantidade)
            print(venda.salvar())

        elif escolha == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
