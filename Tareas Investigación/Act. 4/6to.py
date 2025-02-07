from scipy.optimize import linprog

# Definir los tiempos de cada operación
t1, t2, t3, t4, t5 = 15, 5, 5, 20, 20
n = 6  # Número total de viguetas
traslado_c = 10  # Tiempo de traslado del cortador C

# Definir la función objetivo: minimizar T
c = [1]  # Queremos minimizar T

# Matriz de restricciones
A = [[-1]]  # Restricción de T >= 390
b = [- (n * (t1 + t2 + t3 + t4 + t5))]  # b = -390

# Límites de la variable T (T >= 0)
bounds = [(0, None)]

# Resolver el problema de optimización
resultado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Mostrar resultados
print("Tiempo mínimo total:", resultado.fun, "segundos")
