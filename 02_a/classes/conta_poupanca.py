from .conta_bancaria import contaBancaria
class contaPoupanca(contaBancaria):
    def __init__(self):
        super().__init__()

    def cadastrarCP(self, nome, numeroConta, saldo):
        self.nome = nome
        self.numeroConta = numeroConta
        self.saldo = saldo

    def saque(self, valor, numeroConta):
        if numeroConta == self.numeroConta:
            if (self.saldo - valor) > 0:
                self.saldo = self.saldo - valor
                print('Saque efetuado com sucesso, saldo atual é ' + str(self.saldo))
            else:
                print('Saldo insuficiente.')
