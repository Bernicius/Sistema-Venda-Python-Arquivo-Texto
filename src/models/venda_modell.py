class Venda:
    def __init__(self, codigovenda, data, valortotal, codigocliente):
        self.codigovenda = codigovenda
        self.data = data
        self.valortotal = valortotal
        self.vendacliente = codigocliente
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def __str__(self):
        return (f"Código da Venda: {self.codigovenda}, Data: {self.data}, Valor Total: R${self.valortotal:.2f}, "
                f"Cliente: {self.vendacliente}, Itens: {[str(item) for item in self.itens]}")
