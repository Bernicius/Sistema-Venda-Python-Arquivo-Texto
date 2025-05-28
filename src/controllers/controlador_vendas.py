from src.models.venda_modell import Venda
from src.models.itemVenda_model import ItemVenda
from src.controllers.controlador_cadastro import clientes, produtos

vendas = {}

def salvar_vendas_em_txt():
    with open("vendas.txt", "w") as arquivo:
        for cliente_id, lista_vendas in vendas.items():
            for venda in lista_vendas:
                itens_str = ",".join(
                    [f"{item.codigoproduto}:{item.quantidade}:{item.valor}" for item in venda.itens]
                )
                arquivo.write(f"{venda.codigovenda};{venda.data};{venda.valortotal};{cliente_id};{itens_str}\n")
    print("Vendas salvas com sucesso!")

def carregar_vendas_de_txt():
    global vendas
    try:
        with open("vendas.txt", "r") as arquivo:
            for linha in arquivo:
                if linha.strip():  # Ignorar linhas em branco
                    codigovenda, data, valortotal, cliente_id, itens_str = linha.strip().split(";")
                    venda = Venda(int(codigovenda), data, float(valortotal), int(cliente_id))
                    itens = itens_str.split(",")
                    for item_str in itens:
                        codigoproduto, quantidade, valor = item_str.split(":")
                        venda.adicionar_item(ItemVenda(int(codigoproduto), int(codigovenda), int(quantidade), float(valor)))
                    if int(cliente_id) not in vendas:
                        vendas[int(cliente_id)] = []
                    vendas[int(cliente_id)].append(venda)
        print("Vendas carregadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo de vendas não encontrado. Iniciando com uma lista vazia.")
    except Exception as e:
        print(f"Erro ao carregar vendas: {e}")

def registrar_venda(codigovenda, data, codigo_cliente):
    global vendas

    if codigo_cliente not in clientes:
        print("Cliente não encontrado.")
        return

    venda = Venda(codigovenda, data, 0.0, codigo_cliente)

    while True:
        codigoproduto = int(input("Digite o código do produto (ou 0 para encerrar): "))
        if codigoproduto == 0:
            break

        if codigoproduto not in produtos:
            print("Produto não encontrado.")
            continue

        quantidade = int(input(f"Digite a quantidade para o produto {produtos[codigoproduto].nome}: "))
        valor_unitario = produtos[codigoproduto].preco
        valor_total_item = quantidade * valor_unitario

        item = ItemVenda(codigovenda, codigoproduto, quantidade, valor_total_item)
        venda.adicionar_item(item)

        venda.valortotal += valor_total_item
        print(f"Item {produtos[codigoproduto].nome} adicionado com sucesso!")

    if codigo_cliente not in vendas:
        vendas[codigo_cliente] = []

    vendas[codigo_cliente].append(venda)
    salvar_vendas_em_txt()
    print(f"Venda de código {codigovenda} registrada para o cliente {clientes[codigo_cliente].nome} com sucesso!")

def listar_vendas_cliente(codigo_cliente):
    if codigo_cliente not in clientes:
        print("Cliente não encontrado.")
        return

    if codigo_cliente not in vendas or not vendas[codigo_cliente]:
        print(f"O cliente {clientes[codigo_cliente].nome} não possui vendas registradas.")
        return

    print(f"Vendas do cliente {clientes[codigo_cliente].nome} (Código: {codigo_cliente}):")
    print("=" * 50)

    for venda in vendas[codigo_cliente]:
        print(f"Código da Venda: {venda.codigovenda}, Data: {venda.data}, Valor Total: R${venda.valortotal:.2f}")
        print("Itens:")
        for item in venda.itens:
            produto = produtos.get(item.codigoproduto)
            nome_produto = produto.nome if produto else "Produto não encontrado"
            print(f"- {nome_produto}")

        print("-" * 50)


def mostrar_vendas_cliente(codigo_cliente):
    if codigo_cliente not in clientes:
        print("Cliente não encontrado.")
        return

    if codigo_cliente not in vendas or not vendas[codigo_cliente]:
        print(f"O cliente {clientes[codigo_cliente].nome} não possui vendas registradas.")
        return

    print("=" * 50)
    print(f"NOTA FISCAL - CLIENTE {clientes[codigo_cliente].nome}")
    print("=" * 50)
    print(f"Código do Cliente: {codigo_cliente}")
    print("-" * 50)

    total_geral = 0.0

    for venda in vendas[codigo_cliente]:
        print(f"Venda Código: {venda.codigovenda} | Data: {venda.data}")
        print(f"{'Produto':<20}{'Qtde':<10}{'Valor (R$)':<10}")
        print("-" * 50)

        for item in venda.itens:
            produto = produtos.get(item.codigoproduto)
            nome_produto = produto.nome if produto else "Produto não encontrado"
            print(f"{nome_produto:<20}{item.quantidade:<10}{item.valor:<10.2f}")

        total_geral += venda.valortotal
        print("-" * 50)

    print(f"TOTAL GERAL: R${total_geral:.2f}")
    print("=" * 50)
    print("Obrigado por utilizar nossos serviços!")
    print("=" * 50)
