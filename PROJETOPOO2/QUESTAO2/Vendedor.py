from Funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, idade, genero, salario, matricula, valorVendas, vendas ):
        super(vendedor, self). __init__(self, nome, idade, genero, salario, matricula)
        self.vendas = vendas
        self.valorVendas = valorVendas

    def __str__(self):
        return "Vendedor valorVendas : "  + str(self.valorVendas) + ", vendas :" + str(self.vendas)