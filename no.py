

class No:

    def __init__(self, info: str, linha: int):      

        #Armazenamento da palavra e lista de linhas de ocorrência da palavra no texto.

        self.info: str = info
        self.linhas: list = [linha]

        #Pra fins de simplificação a altura de um nó existente é 1, mesmo que seja nó folha.

        self.altura = 1

        self.esq = None
        self.dir = None

    #Função para contar a frequência de ocorrência da palavra no texto.

    def frequencia(self):
        return len(self.linhas)





    


