# Suma de matrices
# Leer 2 matrices de 3 x 3 y sumar en una matriz

matriz1 = []
print("Ingrese los valores de la primera matriz:")
for i in range(3):
	matriz1.append([])
	for j in range(3):
		matriz1[i].append(int(input(f"Ingrese el valor [{i}][{j}]: ")))

matriz2 = []
print("Ingrese los valores de la segunda matriz:")
for i in range(3):
	matriz2.append([])
	for j in range(3):
		matriz2[i].append(int(input(f"Ingrese el valor [{i}][{j}]: ")))

matrizSuma = []
for i in range(3):
	matrizSuma.append([])
	for j in range(3):
		matrizSuma[i].append(matriz1[i][j] + matriz2[i][j])

print("Matriz resultante de la suma:")
for i in range(3):
	print(matrizSuma[i])
