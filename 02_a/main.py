from classes.conta_corrente import contaCorrente
from classes.conta_poupanca import contaPoupanca

continuar = True
while continuar:
    print('==============================================')
    print('O que você deseja fazer?')
    print('Digite 1 para cadastrar uma conta poupança')
    print('Digite 2 para cadastrar uma conta corrente')
    print('Digite 3 para aumentar o limite de sua conta corrente')
    print('Digite 4 para depositar em sua  conta poupança')
    print('Digite 5 para depositar em sua conta corrente')
    print('Digite 6 para sacar um valor de sua conta poupança')
    print('Digite 7 para sacar um valor de sua conta corrente')
    valorDigitado = input(':: ')

    if valorDigitado == '1':
        conta_poupanca = contaPoupanca()
        conta_poupanca.cadastrarCP(input('Informe o nome do titular: '), input('Informe o número da conta: '), 0.0)
        print('Conta cadastrada com sucesso')

    elif valorDigitado == '2':
        conta_corrente = contaCorrente()
        conta_corrente.cadastrarCC(input('Informe o nome do titular: '), input('Informe o número da conta: '), 0.0)
        print('Conta cadastrada com sucesso')

    elif valorDigitado == '3':
        conta_corrente.aumentarLimite(float(input('Informe o novo limite: ')))
        print('Seu limite de crédito em sua conta corrente agora é de ' + str(conta_corrente.limiteCredito))

    elif valorDigitado == '4':
        conta_poupanca.deposito(input('Informe o valor do depósito: '), input('Informe o número da conta: '))

    elif valorDigitado == '5':
        conta_corrente.deposito(input('Informe o valor do depósito: '), input('Informe o número da conta: '))

    elif valorDigitado == '6':
        conta_poupanca.saque(float(input('Informe o valor a ser sacado: ')), input('Informe o número da conta:'))

    elif valorDigitado == '7':
        conta_corrente.saque(float(input('Informe o valor a ser sacado: ')), input('Informe o número da conta:'))
    else:
        print('Operação inválida.')

    verifica = input('Digite 1 se deseja fazer outra operação ou qualquer outra tecla para sair do sistema: ' )
    coninuar = verifica == '1'
    print('\n \n')
