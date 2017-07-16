class Produto:

    def __init__(self, valor, nome):
        self.valor = valor
        self.nome = nome

    def __str__(self):
        return "Produto Nome: " + self.nome + ", valor: " + str(self.valor)