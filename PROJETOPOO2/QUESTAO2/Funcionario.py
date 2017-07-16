from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, genero, salario, matricula):
        super(Funcionario, self). __init__(self, nome,idade, genero)
        self.matricula = matricula
        self.sarario = salario


    def INSS (self):
        return self.salario * 0,11