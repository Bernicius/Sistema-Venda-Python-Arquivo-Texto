class ItemVenda:
    def __init__(self, codigovenda, codigoproduto, quantidade, valor):
        self.codigovenda = codigovenda
        self.codigoproduto = codigoproduto
        self.quantidade = quantidade
        self.valor = valor

    def __str__(self):
        return f"Código da Venda: {self.codigovenda}, Produto: {self.codigoproduto}, Quantidade: {self.quantidade}, Valor: R${self.valor:.2f}"
