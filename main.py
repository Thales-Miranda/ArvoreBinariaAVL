


from collections import Counter


arq = open("texto_origem.txt", mode="rt", encoding="utf-8")


linha: str = None
contador: int = 0
lista = []






while (linha != "#FIM"):

    linha = arq.readline()
    linha = linha.strip() #limpa espaços em branco e \n
    contador += 1

    lista = linha.split(" ")
    dicionario = Counter(lista)

    print (dicionario)
    print(f"Linha {contador}: {linha}" )





