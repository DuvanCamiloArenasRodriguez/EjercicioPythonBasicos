#Importar
import random

#Funciones
def numAleatorio(lista,listaascendente,listadescendete):
    print("***Listado Original***")
    for i in range (10):
        lista[i] = random.randrange(1,10);
        listaascendente[i] = lista[i]
        listadescendete[i] = lista[i]
        print(lista[i])

def ascendente(listaascendente):
   
    for i  in range(1, 10):
        for j in range(1, 9):
            if listaascendente[j] > listaascendente[j+1]:
                 aux = listaascendente[j]
                 listaascendente[j] = listaascendente[j+1]
                 listaascendente[j+1] = aux

    print("***Lista Ascendente***")
    for i in range(1, 10):
        print(listaascendente[i])

def descendente(listadescendente):
    for i  in range(1, 10):
        for j in range(1,9):
            if listadescendente[j] < listadescendente[j+1]:
                 aux = listadescendente[j]
                 listadescendente[j] = listadescendente[j+1]
                 listadescendente[j+1] = aux

#Código
    print("***Lista Descendente***")
    for i in range(1, 10):
        print(listadescendente[i])
lista = [0] * 11
listaascendente = [0] * 11
listadescendente = [0] * 11

numAleatorio(lista, listaascendente, listadescendente)
ascendente(listaascendente)
descendente(listadescendente)
