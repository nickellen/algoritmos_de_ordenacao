from random import randint
import time

def bubbleSort(lista, fim):
    
    sin = 'false'
    
    for j in range(0, fim):
        for i in range(0 , fim):
            if lista[i] > lista[i+1]:
                troca(lista, i, i+1)
                sin = 'true'
        if (sin=='false'):
            break

def quickSort(lista, fim, inicio=0):
    
    if (inicio < fim):
        pivo = particiona(lista, fim, inicio)
        quickSort(lista, pivo-1, inicio)
        quickSort(lista, fim, pivo+1)
    
def particiona(lista, fim,  inicio): 

    pivo = lista[fim]
    i = inicio
    
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            troca(lista, i, j)
            i+=1
    
    troca(lista , i, fim)
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

        
    esquerda = [0] * (n1)
    direita = [0] * (n2)
    
    for i in range(0 ,  n1):
        esquerda[i] = lista[inicio+i]
    
    for j in range(0 ,  n2):
        direita[j] = lista[meio+1+j]
    
    i = j = 0
    k = inicio
    
    while (i < n1) and (j < n2):
        if esquerda[i] < direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1

    while (i < n1):
        lista[k] = esquerda[i]
        i += 1
        k += 1

    while (j < n2):
        lista[k] = direita[j]
        j += 1
        k += 1
            
def mergeSort2(lista, inicio, meio, fim):
    n1 = meio - inicio + 1
    n2 = fim - meio
        
    esquerda = [0] * (n1+1)
    direita = [0] * (n2+1)
    
    inf = sum(lista)

    for i in range(0 ,  n1):
        esquerda[i] = lista[inicio+i]
    
    for j in range(0 ,  n2):
        direita[j] = lista[meio+1+j]
    
    esquerda[n1] = inf
    direita[n2] = inf
    
    i = j = 0
    
    for k in range(inicio, fim+1):
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1  
            
def criaVetorEmbaralhado(n):
    lista  = [0]*n
    
    for i in range(0,n):
        lista[i] = i
    
    for i in range(0, n-1):
        x = randint(0, n-1)
        troca(lista, i,x)
    
    return lista

def imprimeResultado(algoritmo):
    print(f"Algoritmo {algoritmo.__name__}:\n")
    for n in range(1,5):
        tam = 10**n
        lista  = criaVetorEmbaralhado(tam)
        print(f"Lista de tamanho {10**n}")
        #print(f"Lista desordenada: {lista}")

        inicio = time.time()
        algoritmo(lista, tam -1)
        fim = time.time()
        
        #print("Lista ordenada: ", lista)
        print("Tempo de execução:", fim-inicio,"seg.\n" )
    
def main():
    
    while True:
        print("-------------------------------------------------------------------")
        print("Selecione o algoritmo de ordenação:\n1 - BubbleSort\n2 - QuickSort\n3 - MergeSort")
        print("-------------------------------------------------------------------")
        opcao = int(input(" "))
        
        match opcao:
            case 1:
                imprimeResultado(bubbleSort)
            case 2:
                imprimeResultado(quickSort)
            case 3:
                imprimeResultado(mergeSort)
        
    print("\n\n")

if __name__=="__main__":
    main()
