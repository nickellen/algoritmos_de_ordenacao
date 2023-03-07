#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
void imprimirArray(int n, int* v);

void preencherArray(int n, int* v);

void bubbleSort(int n, int* v);

void quickSort(int a,int b, int* v);

void troca(int a, int b, int* v);

int particiona(int a,int b, int* v);

void mergeSort(int a,int b, int* v);


void main()
{
    int n;
    int *v;
    
    printf("Informe o tamanho do array: ");
    scanf("%d", &n);

    v = (int *) malloc(n * sizeof(int));
    
    preencherArray(n, v);
    quickSort(0,n-1,v);
    imprimirArray(n, v);
    
    free(v);
}

void mergeSort(int a,int b, int* v){
    if (a<b){
        c = (a+b)/2;
        mergeSort(a,c, v);
        mergeSort(c+1,b, v);
        merge(a,b,c, v);
    }
}

merge(int a, int b, int c, int* v){
    
    n1 = c-(a+1);
    n2 = b - c;
    int L[n1+1], R[n2+1];
    
}

void quickSort(int a, int b, int* v){
    
    if (a<b){
        int pivo = particiona(a,b, v);
        quickSort(a,pivo-1, v);
        quickSort(pivo+1,b, v);
    }
    
}

int particiona(int a,int b, int* v){
    
    int x = v[a];
    
    while (a < b){
        while (v[a]< x){
            a++;
        }
        while (v[b]> x){
            b--;
        }
        troca(a,b,v);
    }
    return a;
}

void troca(int a, int b, int* v){
    int tmp = v[a];
    v[a] = v[b];
    v[b] = tmp;
}

void bubbleSort(int n, int* v){
    
    int i, j;
    for (i=0; i<(n-1); i++){
        bool troca = false;
        
        for(j=0; j<(n-1); j++){
            if (v[j] > v[j+1]){
                int tmp = v[j];
                v[j]= v[j+1];
                v[j+1] = tmp;
                troca = true;
            }
        }
        
        if (troca==false){
            break;
        }
    }
}

void imprimirArray(int n, int* v){
    for (int i=0; i<n; i++){
        printf("%-5d" ,v[i]);
    }
}
void preencherArray(int n, int* v){
    int a = 50;
    for (int i=0; i<n; i++){
        v[i] = a--;
    }
}
