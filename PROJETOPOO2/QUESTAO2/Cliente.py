from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, genero, nascimento):
        super(cliente, self). __init__(self, nome, idade, genero, nascimento)
        self.nascimento = nascimento