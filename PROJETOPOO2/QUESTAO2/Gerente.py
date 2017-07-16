from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, idade, genero, salario, matricula, nomeGerente):
        super(Gerente, self). __init__(self, nome, idade, genero, salario, matricula)
        self.nomeGerente = nomeGerente