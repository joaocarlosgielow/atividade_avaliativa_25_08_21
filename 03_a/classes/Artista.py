class Artista:
    def __init__(self):
        self.NomeArtista = ''

    def CadastrarArtista(self, NomeArtista):
        self.NomeArtista = NomeArtista

    def ExcluirArtista(self, NomeArtista):
        if self.NomeArtista == NomeArtista:
            self.NomeArtista = ''
