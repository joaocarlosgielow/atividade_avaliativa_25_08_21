from classes.Catalogo import Catalogo
from classes.Discos import Discos
from classes.Artista import Artista
from classes.Genero import Genero

catalogo = Catalogo('Promoções')

continuar = True
while continuar:
    print('=========================================================')
    print('Informe 1 para cadastrar um artista')
    print('Informe 2 para excluir o artista')
    print('Informe 3 para cadastrar genero')
    print('Informe 4 para excluir genero')
    print('Informe 5 para cadastrar disco')
    print('Informe 6 para excluir disco')
    print('Informe 7 para listar todos os discos')
    print('Informe 8 para listar os discos de uma genero')
    print('Informe 9 para listar os disco de um artista')
    TipoOperacao = input('::')

    if TipoOperacao == '1':
        artista = Artista()
        artista.CadastrarArtista(input('Informe o nome do artista: '))
    elif TipoOperacao == '2':
        artista.ExcluirArtista(input('Informe o nome do artista: '))
    elif TipoOperacao == '3':
        genero = Genero()
        genero.CadastrarGenero(input('Informe o Tipo do Genero: '))
    elif TipoOperacao == '4':
        genero.ExcluirGenero(input('Informe o tipo do genero que deseja excluir: '))
    elif TipoOperacao == '5':
        discos = Discos()
        discos.CadastrarDisco(input('Informe o titulo do disco: '), int(input('Informe o ano: ')), genero, artista)
    elif TipoOperacao == '6':
         discos.ExcluirDisco(input('Informe o titulo do dsico que deseja excluir: '))
    elif TipoOperacao == '7':
        discos.ListarDiscos()
    elif TipoOperacao == '8':
        discos.ListarDiscoGenero(input('Informe o genero que deseja listar: '))
    elif TipoOperacao == '9'
        discos.ListarDiscoArtista(input('Informe o artista: '))
    else:
        print('Informação inválida')

    retorno = input('Informe 1 se deseja fazer mais uma operação, ou qualquer outra tecla para sair')
    continuar = retorno == '1'
    print('\n \n')
