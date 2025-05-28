from src.controllers.controlador_cadastro import clientes, produtos

def mostrar_todos_os_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    # Cabeçalho da tabela
    print("=" * 50)
    print(f"| {'CÓDIGO':<10} | {'NOME':<20} | {'IDADE':<10} |")
    print("=" * 50)

    for cliente in clientes.values():
        print(f"| {cliente.codigo:<10} | {cliente.nome:<20} | {cliente.idade:<10} |")

    print("=" * 50)


def mostrar_todos_os_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("=" * 50)
    print(f"| {'CÓDIGO':<10} | {'NOME':<20} | {'PREÇO (R$)':<15} |")
    print("=" * 50)

    # Linhas da tabela
    for produto in produtos.values():
        print(f"| {produto.codigo:<10} | {produto.nome:<20} | {produto.preco:<15.2f} |")

    # Rodapé da tabela
    print("=" * 50)

