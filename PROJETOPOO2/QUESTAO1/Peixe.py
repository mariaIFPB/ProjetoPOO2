from Animal import Animal
from Calda import Calda

class Peixe(Animal):

    def __init__(self, tipo):
        self.calda = Calda(tipo)

    def __str__(self):
        return "calda tipo: %s" %s (self.calda)
