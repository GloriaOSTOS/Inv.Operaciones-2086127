from scipy.optimize import linprog

# Coeficientes de la función objetivo (minimizar C = 2x + 3y)
c = [2, 3]  # 2 centavos por romper, 3 centavos por soldar

# Restricciones de igualdad (x = y)
A_eq = [[1, -1]]
b_eq = [0]  # x debe ser igual a y

# Restricciones de cantidad mínima de eslabones rotos y soldados (x = 3, y = 3)
A_ub = [[-1, 0], [0, -1], [1, 0], [0, 1]]
b_ub = [-3, -3, 3, 3]  # x >= 3, y >= 3 y no más de 3

# Límites de las variables (x >= 3, y >= 3)
bounds = [(3, 3), (3, 3)]

# Resolver el problema de optimización
resultado = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Mostrar resultados
print("Número óptimo de eslabones rotos:", resultado.x[0])
print("Número óptimo de eslabones soldados:", resultado.x[1])
print("Costo mínimo total:", resultado.fun, "centavos")