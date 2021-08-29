from .conta_bancaria import contaBancaria

class contaCorrente(contaBancaria):
    def __init__(self):
        super().__init__()
        self.limiteCredito = 0.0

    def cadastrarCC(self, nome, numeroConta, saldo):
        self.nome = nome
        self.numeroConta = numeroConta
        self.saldo = saldo

    def aumentarLimite(self, novoLimite):
        self.limiteCredito = novoLimite

    def saque(self, valor, numeroConta):
        if numeroConta == self.numeroConta:
            if ((self.limiteCredito + self.saldo) - valor) > 0:
                self.saldo = self.saldo - valor
                print('Saque efetuado com sucesso, saldo atual é ' + str(self.saldo))
            else:
                print('Saldo insuficiente.')
