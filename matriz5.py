"""
Dada una matriz cuadrada. convertirla a Matriz de identidad.
"""
# Convierte una matriz cuadrada en matriz de identidad y muestra la diagonal en azul.

from colorama import Fore, Style

"""
Dada una matriz cuadrada. convertirla a Matriz de identidad.
"""
# Convierte una matriz cuadrada en matriz de identidad y muestra la diagonal en azul.

from colorama import Fore, Style

n = int(input("Ingrese el tamaño de la matriz: "))
matriz = []
#Creamos la matriz identidad
for i in range(n):
    fila = []
    for j in range(n): 
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)


    #Imprimimos mostrando la diagonal en azul
for i in range(n):
    for j in range(n):
        if i == j:
            print(Fore.BLUE + str(matriz[i][j]) + Style.RESET_ALL, end=" ")
        else:
            print(matriz[i][j], end=" ")
    print()