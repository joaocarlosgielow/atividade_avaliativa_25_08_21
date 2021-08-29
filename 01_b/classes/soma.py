class soma:
    @staticmethod
    def soma(valor):
        if not len(valor) > 1:
            print('favor informar um vetor com mais de uma posição!')
            return
        produtoTotal = 0.0
        for campo in valor:
            produtoTotal = produtoTotal + campo
        return produtoTotal
