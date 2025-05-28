from src.models.cliente_modell import Cliente
from src.models.produto_modell import Produto

clientes = {}
produtos = {}


def salvar_clientes_em_txt():
    with open("clientes.txt", "w") as arquivo:
        for cliente in clientes.values():
            arquivo.write(f"{cliente.codigo};{cliente.nome};{cliente.idade}\n")
    print("Clientes salvos com sucesso!")


def carregar_clientes_de_txt():
    global clientes
    try:
        with open("clientes.txt", "r") as arquivo:
            for linha in arquivo:
                if linha.strip():
                    codigo, nome, idade = linha.strip().split(";")
                    clientes[int(codigo)] = Cliente(int(codigo), nome, int(idade))
        print("Clientes carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo de clientes não encontrado. Iniciando com uma lista vazia.")


def salvar_produtos_em_txt():
    with open("produtos.txt", "w") as arquivo:
        for produto in produtos.values():
            arquivo.write(f"{produto.codigo};{produto.nome};{produto.preco}\n")
    print("Produtos salvos com sucesso!")


def carregar_produtos_de_txt():
    global produtos
    try:
        with open("produtos.txt", "r") as arquivo:
            for linha in arquivo:
                if linha.strip():
                    codigo, nome, preco = linha.strip().split(";")
                    produtos[int(codigo)] = Produto(int(codigo), nome, float(preco))
        print("Produtos carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Iniciando com uma lista vazia.")


def cadastrar_cliente(codigo, nome, idade):
    if codigo in clientes:
        print(f"Erro: Já existe um cliente cadastrado com o código {codigo}.")
        return

    if codigo < 0:
        print("Erro: O código do cliente não pode ser negativo.")
        return

    cliente = Cliente(codigo, nome, idade)
    clientes[codigo] = cliente
    salvar_clientes_em_txt()
    print(f"Cliente {nome} cadastrado com sucesso!")


def cadastrar_produto(codigoproduto, nome, preco):

    if codigoproduto in produtos:
        print(f"Erro: Já existe um produto cadastrado com o código {codigoproduto}.")
        return

    if preco < 0:
        print("Erro: O preço do produto não pode ser negativo.")
        return

    produto = Produto(codigoproduto, nome, preco)
    produtos[codigoproduto] = produto
    salvar_produtos_em_txt()
    print(f"Produto {nome} cadastrado com sucesso!")
