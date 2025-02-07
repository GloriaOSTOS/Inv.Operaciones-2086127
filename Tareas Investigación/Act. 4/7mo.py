from scipy.optimize import linprog
import numpy as np

# Número de puntos
n = 10

# Variables binarias: matriz de tamaño 10x10
c = np.ones(n*n)  # Minimizamos la cantidad de movimientos

# Restricciones de asignación
A_eq = []
b_eq = []

# Cada punto original se mueve a exactamente una nueva posición
for i in range(n):
    fila = np.zeros(n*n)
    for j in range(n):
        fila[i*n + j] = 1
    A_eq.append(fila)
    b_eq.append(1)

# Cada posición final recibe exactamente un punto
for j in range(n):
    fila = np.zeros(n*n)
    for i in range(n):
        fila[i*n + j] = 1
    A_eq.append(fila)
    b_eq.append(1)

# Resolver el problema de optimización
res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0,1)]*(n*n), method='highs')

# Mostrar resultado
print("Número mínimo de movimientos necesarios:", int(res.fun))

# Mostrar la solución óptima con la pirámide invertida
piramide_inicial = [
    [1, 2, 3, 4],
    [5, 6, 7],
    [8, 9],
    [10]
]

piramide_invertida = [
    [10],
    [8, 9],
    [5, 6, 7],
    [1, 2, 3, 4]
]

print("Pirámide inicial:")
for fila in piramide_inicial:
    print(" ".join(map(str, fila)))

print("\nPirámide invertida:")
for fila in piramide_invertida:
    print(" ".join(map(str, fila)))