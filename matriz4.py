#Multiplicacion de matrices 2x2
matrizA = []
matrizB = []
matrizC = []
print("Ingrese los valores de la primera matriz (2x2):")
for i in range(2):
    fila = []
    for j in range(2):
       valor = int(input(f"Ingrese el valor para la posición [{i+1}][{j+1}]: "))
       fila.append(valor)
    matrizA.append(fila)

    print("Ingrese los valores de la segunda matriz (2x2):")
for i in range(2):
    fila = []
    for j in range(2):
       valor = int(input(f"Ingrese el valor para la posición [{i+1}][{j+1}]: "))
       fila.append(valor)
    matrizB.append(fila)

    #Multiplicacion de matrices
for i in range(2):
    fila = []
    for j in range(2):
        valor = 0
        for k in range(2):
            valor += matrizA[i][k] * matrizB[k][j]
        fila.append(valor)
    matrizC.append(fila)

print("Matriz resultante de la multiplicación:")
