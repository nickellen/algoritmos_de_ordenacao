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
        pivo = particiona2(lista, inicio, fim)
        quickSort(lista, inicio, pivo-1)
        quickSort(lista, pivo+1, fim)
    
def particiona(lista, inicio, fim): 

    x = lista[fim]       

    while (inicio < fim):
        
        if (lista[inicio] == lista[fim]) and (lista[fim]== x):
            inicio+=1
            continue

        while (lista[inicio] < x): 
            inicio+=1               
            
        while (lista[fim] > x): 
            fim-=1    

        troca(lista, inicio, fim) 

    return inicio 
    
    
def particiona2(lista, inicio, fim): 

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

teste ={
    'lista1' : [0,75, 1, 3, 7, 9,12,13],
    'lista2' : [10,9,8,7,6,5,4,3,188, 2,1,9,8,7,6,5,4,3,188, 2,1],
    'lista3' : [1,2,3,4,5,6,7,8,9,10],
    'lista4' : [10,9,8,7,6,5,4,3,2,1,0]
}

for i in teste:
    lista = teste[i]
    print(lista)
    quickSort(lista)
    print(lista, "\n")
