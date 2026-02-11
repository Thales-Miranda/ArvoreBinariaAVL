from no import No

class AVL:

    def __init__(self):
        self.__raiz = None

    def __altura(self, no):
        if(no == None):
            return 0
        else:
            return no.altura
        




    #Calculo do fator de balanceamento para assegurar eficiência e garantir uma ávore AVL
    #Importância do sinal para saber para qual lado está desbalanceado +2 -2

    def __fatorBalanceamento(self, no):
        return self.__altura(no.esq) - self.__altura(no.dir)
    
    #Rotações para balanceamento e recalculo da altura

    def __maior(self, A, B):

        if A > B:
            return A
        else:
            return B

    def __RotacaoLL(self, A):
        print('RotacaoLL: ',A.info);
        B = A.esq
        A.esq = B.dir
        B.dir = A
        A.altura = self.__maior(self.__altura(A.esq),self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq),A.altura) + 1
        #A = B
        return B

    def __RotacaoRR(self, A):
        print('RotacaoRR: ',A.info);
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self.__maior(self.__altura(A.esq),self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.dir),A.altura) + 1
        #A = B
        return B

    def __RotacaoLR(self, A):
        A.esq = self.__RotacaoRR(A.esq)
        A = self.__RotacaoLL(A)
        return A

    def __RotacaoRL(self, A):
        A.dir = self.__RotacaoLL(A.dir)
        A = self.__RotacaoRR(A)
        return A
    




# Inserção da palavra no No
    def __insereValor(self, atual, valor, linha):
        # Primeiro No (raiz ou folha alcançada)
        if atual == None: 
            novo = No(valor, linha) # Passando valor e linha para o construtor do seu No
            return novo
        
        if valor < atual.palavra: # Usando .palavra conforme seu No
            atual.esq = self.__insereValor(atual.esq, valor, linha)
            if self.__fatorBalanceamento(atual) >= 2:
                if valor < atual.esq.palavra:
                    atual = self.__RotacaoLL(atual)
                else:
                    atual = self.__RotacaoLR(atual)

        elif valor > atual.palavra:
            atual.dir = self.__insereValor(atual.dir, valor, linha)
            if self.__fatorBalanceamento(atual) <= -2:
                if valor > atual.dir.palavra:
                    atual = self.__RotacaoRR(atual)
                else:
                    atual = self.__RotacaoRL(atual)
        
        else:
            # Caso a palavra já exista (valor == atual.palavra)
            # Regra do enunciado: linha aparece apenas uma vez no índice
            if linha not in atual.linhas:
                atual.linhas.append(linha)

        atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1
        return atual

    def insere(self, valor, linha):
        # Para o índice remissivo, não retornamos False se existir.
        # Nós sempre chamamos o __insereValor para atualizar a lista de linhas.
        self.__raiz = self.__insereValor(self.__raiz, valor, linha)



#Busca da Palavra (no.palavra)

    def busca(self, valor):
        if(self.__raiz == None):
            return None

        atual = self.__raiz
        while(atual != None):
            if(valor == atual.info):
                return atual
            #Mostra informação do no (palavra e lista)

            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq

        return None
    




#Remoção do No

    def __procuraMenor(self, atual):
        no = atual
        while no.esq is not None:
            no = no.esq
        return no

    def __removeValor(self, atual, valor):

        if atual == None:
            return None

        #Procurar o nó
        if valor < atual.info:
            atual.esq = self.__removeValor(atual.esq, valor)

        elif valor > atual.info:
            atual.dir = self.__removeValor(atual.dir, valor)

        else:
        #Nó encontrado

        # Caso 1 filho ou nenhum
            if atual.esq == None:
                return atual.dir
            elif atual.dir == None:
                return atual.esq

        # Caso 2 filhos
            temp = self.__procuraMenor(atual.dir)
            atual.info = temp.info
            atual.dir = self.__removeValor(atual.dir, temp.info)

    #Atualiza altura
        atual.altura = self.__maior(
        self.__altura(atual.esq),
        self.__altura(atual.dir)
    ) + 1

    #Balanceamento
        fb = self.__fatorBalanceamento(atual)

    # Pesado esquerda
        if fb >= 2:
            if self.__altura(atual.esq.esq) >= self.__altura(atual.esq.dir):
                return self.__RotacaoLL(atual)
            else:
                return self.__RotacaoLR(atual)

    # Pesado direita
        if fb <= -2:
            if self.__altura(atual.dir.dir) >= self.__altura(atual.dir.esq):
                return self.__RotacaoRR(atual)
            else:
                return self.__RotacaoRL(atual)

        return atual





#Ordem Alfabética

    def __emOrdem(self,raiz):
        if(raiz != None):
            self.__emOrdem(raiz.esq)
            print(raiz.info, end=' ')
            self.__emOrdem(raiz.dir)

    def emOrdem(self):
        if(self.__raiz != None):
            self.__emOrdem(self.__raiz)


#Palavra mais frequente

    def palavra_mais_frequente(self):
        self.max_freq = 0
        self.palavra_mais_frequente = ""

        def percorrer(no):
            if no:
                percorrer(no.esq)
                freq_atual = len(no.linhas)
                if freq_atual > self.max_freq:
                    self.max_freq = freq_atual
                    self.palavra_mais_frequente = no.palavra
                percorrer(no.dir)

        percorrer(self.__raiz)
        return self.palavra_mais_frequente, self.max_freq







