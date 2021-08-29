from classes.unidade_federativa import unidade_federativa

continuar = True
unidadeFederativa = unidade_federativa()

while continuar:
    print('==============================')
    print('O que deseja fazer?')
    print('Digite 1 se quiser listar todos os estados')
    print('Digite 2 se quiser consultar um estado por sua sigla')
    oqueFazer = input(':: ')

    if oqueFazer == '1':
        print(unidadeFederativa.get_lista_uf())
    elif oqueFazer == '2':
        print(unidadeFederativa.get_uf(input('Informe a sigla da UF: ')))
    else:
        print('OPÇÃO INVÁLIDA!!')

    validarContinuar = input('Digite 1 se deseja fazer mais uma operação: ')
    continuar = validarContinuar == '1'
    print('\n \n')
