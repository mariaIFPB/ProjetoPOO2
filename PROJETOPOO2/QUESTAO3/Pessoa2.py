class Pessoa():
    def __init__(self, nome, endereco, tel):
        self.nome = nome
        self.endereco = endereco
        self.tel = tel

    def __str__(self):
        return print(self.nome + " ",self.endereco + " ", self.tel)