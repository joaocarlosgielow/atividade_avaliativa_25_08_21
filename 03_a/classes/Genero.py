class Genero:
    def __init__(self):
        self.TipoGenero = ''

    def CadastrarGenero(self, TipoGenero):
        self.TipoGenero = TipoGenero

    def ExcluirGenero(self, TipoGenero):
        if self.TipoGenero == TipoGenero:
            self.TipoGenero = ''
