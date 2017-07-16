from Animal import Animal

class Cachorro():

    def __init__(self, raca, nome, peso, habitat):
        super(Cachorro, self).__init__(nome, peso, habitat)
        self.raca = raca

    def  brincar (self):
       print("cachorro brincando.")

    def vigiar(self):
        print("cachorro vigiando.")

