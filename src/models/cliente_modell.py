class Cliente:
    def __init__(self, codigo, nome, idade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Idade: {self.idade}"
