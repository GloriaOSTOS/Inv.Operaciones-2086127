from scipy.optimize import linprog

# Definir los costos de los boletos como los coeficientes de la función objetivo
c = [400, 300, 300, 320]  # x1: regular, x2: ida, x3: vuelta, x4: redondo con descuento

# Definir las restricciones de desigualdad (matriz A y vector b)
A = [
    [-1, -1,  0, -1],  # Restricción para las idas (>= 5)
    [-1,  0, -1, -1]   # Restricción para las vueltas (>= 5)
]
b = [-5, -5]  # Restricciones negativas para que sean >= al resolver

# Definir las cotas de las variables (no negativas)
x_bounds = (0, None)  # Cada variable debe ser >= 0
bounds = [x_bounds] * 4

# Resolver el problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

# Mostrar los resultados
if result.success:
    print("\nSolución óptima encontrada:")
    print(f"x1 (boletos regulares FYV-DEN-FYV): {result.x[0]:.2f}")
    print(f"x2 (boletos de ida FYV-DEN): {result.x[1]:.2f}")
    print(f"x3 (boletos de vuelta DEN-FYV): {result.x[2]:.2f}")
    print(f"x4 (boletos redondos DEN-FYV-DEN con descuento): {result.x[3]:.2f}")
    print(f"Costo total mínimo: ${result.fun:.2f}")
else:
    print("No se encontró solución óptima.")
