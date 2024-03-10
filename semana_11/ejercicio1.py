def buscar_valor(matriz, valor):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #recorremos cada una de las posiciones hasta encontrar el valor buscado
            if matriz[i][j] == valor:
                return True, i, j
    return False, None, None

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#modificamos el valor según necesitemos
valor_a_buscar = 6

# Realizar la búsqueda
encontrado, fila, columna = buscar_valor(matriz, valor_a_buscar)


if encontrado:
    print(f"El valor {valor_a_buscar} fue encontrado en la posición ({fila}, {columna}) de la matriz")
else:
    print(f"El valor {valor_a_buscar} no fue encontrado en la matriz.")
