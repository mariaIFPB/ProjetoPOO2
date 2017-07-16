from Produto import Produto
from Vendedor import Vendedor

def main():
    Vendedor = Vendedor("Roberto", 30, "masculino", 2000, 123, 50, 4, [
    Produto("violao", 250),
    Produto("ventilador", 150),
    Produto("fone", 100)])

print(Vendedor)
print("INSS :" + str(Vendedor.INSS()))

if(__name__ == "__sair__"):
    main()