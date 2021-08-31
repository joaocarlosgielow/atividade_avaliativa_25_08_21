from Artista import Artista
from Genero import Genero

class Discos:
    def __init__(self):
        self.Titulo = ''
        self.Ano = 0
        self.Genero = Genero()
        self.Artista = Artista()

    def CadastrarDisco(self, Titulo, Ano, Genero, Artista):
        self.Titulo = Titulo
        self.Ano = Ano
        self.Genero = Genero
        self.Artista = Artista

    def ExcluirDisco(self, Titulo):
        if self.Titulo == Titulo:
            self.Titulo = ''
            self.Ano = 0
            self.Genero = Genero()
            self.Artista = Artista()

    def ListarDiscos(self):
        return 'Disco de titulo: ' + self.Titulo + ', do ano: ' + str(self.Ano) + ', do genero: ' + self.Genero.TipoGenero + ', do artista: ' + self.Artista.NomeArtista

    def ListarDiscoGenero(self, Genero):
        if self.Genero.TipoGenero == Genero:
            return 'Disco de titulo: ' + self.Titulo + ', do ano: ' + str(self.Ano) + ', do genero: ' + self.Genero.TipoGenero + ', do artista: ' + self.Artista.NomeArtista

    def ListarDiscoArtista(self, Artista):
        if self.Artista.NomeArtista == Artista:
            return 'Disco de titulo: ' + self.Titulo + ', do ano: ' + str(self.Ano) + ', do genero: ' + self.Genero.TipoGenero + ', do artista: ' + self.Artista.NomeArtista
