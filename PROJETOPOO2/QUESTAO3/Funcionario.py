from Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, codigoSetor, salarioBase, imposto):
        self.codigoSetor = codigoSetor
        self.salarioBase = salarioBase
        self.imposto = imposto

    def calcularSalarioTotal( salarioBase, imposto):
        salarioTotal = salarioBase - imposto