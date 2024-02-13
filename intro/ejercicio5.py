matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

for fila in matriz:
    suma = sum(fila[:3])  # Calcula la suma de los tres primeros elementos de la fila
    fila[3] = suma  # Actualiza el cuarto elemento de la fila con la suma calculada

print(matriz)
