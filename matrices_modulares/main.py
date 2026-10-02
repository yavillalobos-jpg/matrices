def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no valida. Ingresa un numero entero.")


def leer_dimensiones(nombre="la matriz"):
    filas = leer_entero(f"Numero de filas de {nombre}: ", 1)
    columnas = leer_entero(f"Numero de columnas de {nombre}: ", 1)
    return filas, columnas


def leer_matriz(nombre, filas, columnas):
    matriz = []
    print(f"Ingresa los valores de {nombre}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = leer_entero(f"Valor [{i + 1}][{j + 1}]: ")
            fila.append(valor)
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


def mostrar_una_matriz():
    filas, columnas = leer_dimensiones()
    mostrar_matriz(leer_matriz("la matriz", filas, columnas))


def multiplicar_por_escalar():
    filas, columnas = leer_dimensiones()
    matriz = leer_matriz("la matriz", filas, columnas)
    escalar = leer_entero("Ingresa el escalar: ")
    resultado = [[valor * escalar for valor in fila] for fila in matriz]
    print("Resultado de la multiplicacion por escalar:")
    mostrar_matriz(resultado)


def sumar_matrices():
    filas, columnas = leer_dimensiones("las matrices")
    matriz_a = leer_matriz("la primera matriz", filas, columnas)
    matriz_b = leer_matriz("la segunda matriz", filas, columnas)
    resultado = [
        [matriz_a[i][j] + matriz_b[i][j] for j in range(columnas)]
        for i in range(filas)
    ]
    print("Resultado de la suma:")
    mostrar_matriz(resultado)


def multiplicar_matrices():
    filas_a, columnas_a = leer_dimensiones("la primera matriz")
    matriz_a = leer_matriz("la primera matriz", filas_a, columnas_a)

    while True:
        filas_b = leer_entero("Numero de filas de la segunda matriz: ", 1)
        columnas_b = leer_entero("Numero de columnas de la segunda matriz: ", 1)
        if filas_b == columnas_a:
            break
        print(
            "No se pueden multiplicar: las columnas de la primera matriz "
            "deben coincidir con las filas de la segunda."
        )

    matriz_b = leer_matriz("la segunda matriz", filas_b, columnas_b)
    resultado = []
    for i in range(filas_a):
        fila = []
        for j in range(columnas_b):
            valor = sum(matriz_a[i][k] * matriz_b[k][j] for k in range(columnas_a))
            fila.append(valor)
        resultado.append(fila)
    print("Resultado de la multiplicacion:")
    mostrar_matriz(resultado)


def crear_matriz_identidad():
    tamano = leer_entero("Ingresa el tamano de la matriz cuadrada: ", 1)
    matriz = [
        [1 if i == j else 0 for j in range(tamano)]
        for i in range(tamano)
    ]
    print("Matriz identidad:")
    mostrar_matriz(matriz)


def main():
    opciones = {
        "1": ("Mostrar una matriz", mostrar_una_matriz),
        "2": ("Multiplicar una matriz por un escalar", multiplicar_por_escalar),
        "3": ("Sumar dos matrices", sumar_matrices),
        "4": ("Multiplicar dos matrices", multiplicar_matrices),
        "5": ("Crear una matriz identidad", crear_matriz_identidad),
    }

    while True:
        print("\n--- OPERACIONES CON MATRICES ---")
        for numero, (descripcion, _) in opciones.items():
            print(f"{numero}. {descripcion}")
        print("0. Salir")

        opcion = input("Selecciona una opcion: ").strip()
        if opcion == "0":
            print("Programa finalizado.")
            break
        if opcion not in opciones:
            print("Opcion no valida. Selecciona un numero del 0 al 5.")
            continue
        opciones[opcion][1]()


if __name__ == "__main__":
    main()