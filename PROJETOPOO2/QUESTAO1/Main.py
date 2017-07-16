from Cachorro import Cachorro
from Peixe import Peixe
from Animal import Animal

def main():
    a1 = Cachorro("vira lata", "bil", "15", "casa")
    a1.brincar()
    a1.vigiar()

    a2 = Peixe("pequena")
    a2.mover()
    a2.comunicar()



if __name__ == '__main__':
    main()
