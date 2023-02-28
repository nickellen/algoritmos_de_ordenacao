def mergeSort(lista, inicio , fim ):
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
    
teste = {
        'lista1':[10,9,8,7,6,5,4,3,2,1], 
        'lista2':[90,55,7,0,15,4,9,78,4,4,0,87],
        'lista3':[1,2,4,5,6,7,8,9] 
}

for i in teste:
    lista = teste[i]
    print(lista)
    mergeSort(lista, 0 , len(lista))
    print(lista, "\n")
