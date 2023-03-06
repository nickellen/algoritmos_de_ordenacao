from random import randint
import time

def bubbleSort(lista, fim):

    for j in range(0, fim):
        for i in range(0 , fim):
            if lista[i] > lista[i+1]:
                troca(lista, i, i+1)

def quickSort(lista, fim=None, inicio=0):

    if (fim==None):
        fim = len(lista)-1
    
    if (inicio < fim):
        pivo = particiona(lista, fim, inicio)
        quickSort(lista, pivo-1, inicio)
        quickSort(lista, fim, pivo+1)
    
def particiona(lista, fim,  inicio): 

    pivo = lista[inicio]
    i = fim
    
    for j in range(fim, inicio, -1):
        if lista[j] >= pivo:
            troca(lista, i, j)
            i-=1
    
    troca(lista , i, inicio)
    return i

def troca(lista, a, b):
    tmp = lista[a]
    lista[a] = lista[b]
    lista[b] = tmp
    
def mergeSort(lista, fim, inicio=0):
        
    if inicio < fim:
        meio = (fim + inicio)//2
        mergeSort(lista, meio, inicio)
        mergeSort(lista,fim, meio+1)
        merge(lista, inicio, meio, fim)
        
def merge(lista, inicio, meio, fim):
    n1 = meio - inicio + 1
    n2 = fim - meio
    
    inf = 0
    for i in lista:
        inf+=i
        
    esquerda = [0] * (n1+1)
    direita = [0] * (n2+1)
    
    for i in range(0 ,  n1):
        esquerda[i] = lista[inicio+i]
    
    for j in range(0 ,  n2):
        direita[j] = lista[meio+1+j]
        
    esquerda[n1] = inf
    direita[n2] = inf
    
    i = 0
    j = 0
    
    for n in range(inicio, fim+1):
        if (esquerda[i] <= direita[j]):
            lista[n] = esquerda[i]
            i+=1
        else:
            lista[n] = direita[j]
            j+=1
            
def criaVetorEmbaralhado(n):
    lista  = [0]*n
    
    for i in range(0,n):
        lista[i] = i
    
    for i in range(0, n-1):
        x = randint(0, n-1)
        troca(lista, i,x)
    
    return lista

def imprimeListas(algoritmo):
    print(f"Algoritmo {algoritmo.__name__}:\n")
    for n in range(1,5):
        tam = 10**n
        lista  = criaVetorEmbaralhado(tam)
        print(f"Lista desordenada (tamanho {10**n}): {lista}")
        
        inicio = time.time()
        algoritmo(lista, tam -1)
        fim = time.time()
        
        print("Lista ordenada: ", lista)
        print("Tempo de execução:", fim-inicio,"seg.\n" )
    
def main():
    
    print("\n\n")
    while True:
        print("-------------------------------------------------------------------")
        print("Selecione o algoritmo de ordenação:\n1 - BubbleSort\n2 - QuickSort\n3 - MergeSort")
        print("-------------------------------------------------------------------")
        opcao = int(input(" "))
        
        match opcao:
            case 1:
                imprimeListas(bubbleSort)
            case 2:
                imprimeListas(quickSort)
            case 3:
                imprimeListas(mergeSort)
                    
if __name__=="__main__":
    main()
