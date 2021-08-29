class contaBancaria:
    def __init__(self):
        self.nome = ''
        self.numeroConta = ''
        self.saldo = 0.0

    def deposito(self, valor, numeroConta):
        if self.numeroConta == numeroConta:
            self.saldo = self.saldo + float(valor)
            print('Depósito efetuado com sucesso, saldo atual é ' + str(self.saldo))

    def saque(self, valor, numeroConta):
        if self.numeroConta == numeroConta:
            self.saldo = self.saldo - valor
