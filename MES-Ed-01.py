from random import randint

def bubbleSort(lista, fim = None):

    if (fim==None):
        fim = len(lista)
    
    for j in range(0, fim-1):
        for i in range(0 , fim - 1):
            if lista[i] > lista[i+1]:
                troca(lista, i, i+1)

def quickSort(lista, inicio=0, fim=None):

    if (fim==None):
        fim = len(lista)-1
    
    if (inicio < fim):
        pivo = particiona(lista, inicio, fim)
        quickSort(lista, inicio, pivo-1)
        quickSort(lista, pivo+1, fim)
    
def particiona(lista, inicio, fim): 

    pivo = lista[inicio]
    i = fim
    
    for j in range(fim, inicio, -1):
        if lista[j] >= pivo:
            troca(lista, i, j)
            i-=1
    
    troca(lista , inicio, i)
    return i

def troca(lista, a, b):
    tmp = lista[a]
    lista[a] = lista[b]
    lista[b] = tmp

def mergeSort(lista, inicio = 0 , fim = None):
    
    if (fim==None):
        fim = len(lista)
        
    if (fim-inicio)>1:
        meio = (fim + inicio)//2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    
    inf = 0
    for i in lista:
        inf+=i
    
    lista1 = lista[inicio:meio] + [inf]
    lista2 = lista[meio:fim] + [inf]
    
    i = 0
    j = 0
    
    for n in range(inicio, fim):
        if (lista1[i] < lista2[j]):
            lista[n] = lista1[i]
            i+=1
        else:
            lista[n] = lista2[j]
            j+=1
def criaVetorEmbaralhado(n):
    lista  = [0]*n
    
    for i in range(0,n):
        lista[i] = i
    
    for i in range(0, n-1):
        x = randint(0, n-1)
        troca(lista, i,x)
    
    return lista
    
    
def main():
    lista  = criaVetorEmbaralhado(9999)
    lista1  = criaVetorEmbaralhado(9999)
    lista2 = criaVetorEmbaralhado(9999)
    
    bubbleSort(lista)
    quickSort(lista1)
    mergeSort(lista2)
    print(lista, "\n")
    print(lista1, "\n")
    print(lista2)
    
    
if __name__=="__main__":
    main()
