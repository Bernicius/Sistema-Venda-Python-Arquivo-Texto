def menu_principal():
    vermelho_forte = "\033[1;31m"
    reset_cor = "\033[0m"

    mensagem = f'''
    {vermelho_forte}[1] Cadastrar Cliente
    [2] Mostrar todos os clientes
    [3] Cadastrar Produto
    [4] Mostrar Produtos
    [5] Listar Venda de um determinado cliente
    [6] Mostrar todas as vendas de um cliente
    [7] Efetuar uma venda para um cliente
    [8] Encerrar programa{reset_cor}
    '''

    print(mensagem)
    opcao = int(input('Digite sua opção: '))
    return opcao


def capturar_dados_cliente():
    codigo = int(input("Digite o código do cliente: "))
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    return codigo, nome, idade

def capturar_dados_produto():
    codigoproduto = int(input("Digite o código do produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    return codigoproduto, nome, preco
