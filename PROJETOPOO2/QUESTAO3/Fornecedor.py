from Pessoa2 import Pessoa
class Fornecedor(Pessoa):
    def __init__(self, valorCredito, valorDivida):
        super(Fornecedor, self).__init__(nome, endereco, tel)
        self.valorCredito = valorCredito
        self.valorDivida = valorDivida

    def obterSaldo(self, valorCredito, valorDivida):
        saldo = valorCredito - valorDivida
        return (saldo)