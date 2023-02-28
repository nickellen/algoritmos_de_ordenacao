def quickSort(lista, inicio, fim):
    
    if (inicio < fim):
        pivo = particiona(lista, inicio, fim)
        quickSort(lista, inicio, pivo)
        quickSort(lista, pivo+1, fim)
    
def particiona(lista,inicio, fim):
    x = lista[fim]
    
    
    
teste = {
        'lista1':[10,9,8,7,6,5,4,3,2,1], 
        'lista2':[90,55,7,0,15,4,9,78,4,4,0,87],
        'lista3':[1,2,4,5,6,7,8,9] 
}

for i in teste:
    lista = teste[i]
    print(lista)
    quickSort(lista, 0 , len(lista))
    print(lista, "\n")
