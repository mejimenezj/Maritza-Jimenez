def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenar_fila(matriz, fila):
    bubble_sort(matriz[fila])

matriz = [
    [9, 4, 7,15],
    [3,23, 6, 12],
    [8,2, 5,25],
    [6, 3, 15,1]
]


print("Matriz original:")
for fila in matriz:
    print(fila)


fila_a_ordenar = int(input("Ingrese el número de la fila que desea ordenar (Comienza con la fila l ): "))

# Verificar si la fila seleccionada es válida
if 0 <= fila_a_ordenar-1 < len(matriz):
    # Ordenar la fila seleccionada usando Bubble Sort
    ordenar_fila(matriz, fila_a_ordenar-1)

    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
    else:
        print("Número de fila no válido.")    
