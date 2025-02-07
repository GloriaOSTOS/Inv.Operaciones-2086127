from scipy.optimize import linprog

# Coeficientes de la función objetivo (tiempos de los viajes)
# Tiempos de los viajes:
# [Amy y Jim cruzan, Amy regresa, John y Kelly cruzan, Jim regresa, Amy y Jim cruzan de nuevo]
c = [2, 1, 10, 2, 2]

# Matriz de restricciones para asegurar que cada persona cruce exactamente una vez
A_eq = [
    [1, 0, 0, 0, 0],  # Viaje 1: Amy y Jim cruzan
    [0, 1, 0, 0, 0],  # Regreso 1: Amy regresa
    [0, 0, 1, 0, 0],  # Viaje 2: John y Kelly cruzan
    [0, 0, 0, 1, 0],  # Regreso 2: Jim regresa
    [0, 0, 0, 0, 1],  # Viaje 3: Amy y Jim cruzan nuevamente
]
b_eq = [1, 1, 1, 1, 1]  # Cada viaje debe realizarse una vez

# Restricciones de no negatividad
bounds = [(0, 1)] * 5  # Los valores de las variables son binarias (0 o 1)

# Resolver el problema
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Imprimir resultados
print("Resultados:")
print(f"Tiempo total mínimo: {result.fun:.2f} minutos")
print("Detalles de los viajes:")
print(f"Amy y Jim cruzan: {result.x[0]:.2f}")
print(f"Amy regresa: {result.x[1]:.2f}")
print(f"John y Kelly cruzan: {result.x[2]:.2f}")
print(f"Jim regresa: {result.x[3]:.2f}")
print(f"Amy y Jim cruzan nuevamente: {result.x[4]:.2f}")


