from src.controllers.controlador_cadastro import (
    cadastrar_cliente,
    cadastrar_produto,
    carregar_clientes_de_txt,
    carregar_produtos_de_txt,
    salvar_clientes_em_txt,
    salvar_produtos_em_txt,
)
from src.controllers.controlador_vendas import (
    registrar_venda,
    listar_vendas_cliente,
    mostrar_vendas_cliente,
    carregar_vendas_de_txt,
    salvar_vendas_em_txt,
)
from src.view.mostrar_menus import menu_principal, capturar_dados_cliente, capturar_dados_produto
from src.view.mostrar_dicionarios import mostrar_todos_os_clientes, mostrar_todos_os_produtos

if __name__ == "__main__":

    carregar_clientes_de_txt()
    carregar_produtos_de_txt()
    carregar_vendas_de_txt()

    op = 0
    while op != 8:
        op = menu_principal()
        if op == 1:
            codigo, nome, idade = capturar_dados_cliente()
            cadastrar_cliente(codigo, nome, idade)
        elif op == 2:
            mostrar_todos_os_clientes()
        elif op == 3:
            codigoproduto, nome, preco = capturar_dados_produto()
            cadastrar_produto(codigoproduto, nome, preco)
        elif op == 4:
            mostrar_todos_os_produtos()
        elif op == 5:
            codigo_cliente = int(input("Digite o código do cliente para listar as vendas: "))
            listar_vendas_cliente(codigo_cliente)
        elif op == 6:
            codigo_cliente = int(input("Digite o código do cliente: "))
            mostrar_vendas_cliente(codigo_cliente)
        elif op == 7:
            codigovenda = int(input("Digite o código da venda: "))
            data = input("Digite a data da venda (dd/mm/aaaa): ")
            codigo_cliente = int(input("Digite o código do cliente: "))
            registrar_venda(codigovenda, data, codigo_cliente)
        elif op == 8:

            salvar_clientes_em_txt()
            salvar_produtos_em_txt()
            salvar_vendas_em_txt()
            exit("Programa finalizado")
