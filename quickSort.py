def bubbleSort(lista, fim = None):

    if (fim==None):
        fim = len(lista)

    for i in range(0 , fim - 1):
        for j in range(0, fim-1): 
            if lista[i] > lista[j]:
                troca(lista, i, j)

def quickSort(lista, inicio=0, fim=None):

    if (fim==None):
        fim = len(lista)-1
    
    if (inicio < fim):
        pivo = particiona(lista, inicio, fim)
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


def troca(lista, a, b):
    tmp = lista[a]
    lista[a] = lista[b]
    lista[b] = tmp


teste ={
    'lista1' : [0,75, 1, 3, 7, 9,12,13],
    'lista2' : [10,9,8,7,6,5,4,3,188, 2,1,9,8,7,6,5,4,3,188, 2,1],
    'lista3' : [1,2,3,4,5,6,7,8,9,10],
    'lista4' : [10,9,8,7,6,5,4,3,2,1,0]
}

for i in teste:
    lista = teste[i]
    print(lista)
    bubbleSort(lista)
    print(lista, "\n")
