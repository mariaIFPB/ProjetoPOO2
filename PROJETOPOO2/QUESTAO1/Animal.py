class Animal():
    def __init__(self, nome, peso, habitat):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat

    def mover(self):
        print(self.nome + " movendo-se de forma genérica.")

    def comunicar(self):
        print(self.nome + " comunicando de forma genérica.")

    def __str__(self):
        return print(self.nome + " ",self.peso + " ", self.habitat)
