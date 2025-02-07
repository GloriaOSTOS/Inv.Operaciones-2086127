from scipy.optimize import linprog

# Coeficientes de la función objetivo (minimizar el promedio de bateo)
c = [0.3, 0.1, 0.2, 0.5]  # Coeficientes de payoff para x1y1, x1y2, x2y1, x2y2

# Restricciones de probabilidad (suma de probabilidades de Jim y Joe)
A_eq = [
    [1, 1, 0, 0],  # x1 + x2 = 1 (Jim)
    [0, 0, 1, 1]   # y1 + y2 = 1 (Joe)
]
b_eq = [1, 1]

# Restricciones de no negatividad para todas las variables
x_bounds = (0, None)

# Resolver el problema de optimización
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[x_bounds] * 4, method='highs')

# Mostrar resultados
print("Resultados:")
print(f"x1 (Jim - bola rápida): {result.x[0]:.2f}")
print(f"x2 (Jim - curva): {result.x[1]:.2f}")
print(f"y1 (Joe - se prepara para bola rápida): {result.x[2]:.2f}")
print(f"y2 (Joe - se prepara para curva): {result.x[3]:.2f}")
print(f"Valor óptimo (promedio de bateo): {result.fun:.2f}")
print(f"Estado del optimizador: {result.message}")

