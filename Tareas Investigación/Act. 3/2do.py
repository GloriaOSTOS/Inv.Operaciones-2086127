from scipy.optimize import minimize

# Definir el área negativa como función objetivo para maximización
# f(w) = -w * h, pero h = (L/2) - w, entonces:
def area_negativa(w, L):
    h = (L / 2) - w
    return -(w * h)  # Negativo porque scipy minimiza

# Parámetro: longitud del alambre
L = 20  # Puedes cambiar este valor

# Restricciones y límites
bounds = [(0, L / 2)]  # w debe estar entre 0 y L/2

# Valor inicial para w
w_inicial = [L / 4]  # Punto medio como inicio

# Resolver el problema de optimización
resultado = minimize(area_negativa, w_inicial, args=(L,), bounds=bounds, method='SLSQP')

# Extraer resultados
w_optimo = resultado.x[0]
h_optimo = (L / 2) - w_optimo
area_maxima = -resultado.fun

# Mostrar resultados
print("\nSolución óptima:")
print(f"Ancho óptimo (w): {w_optimo:.2f} pulgadas")
print(f"Altura óptima (h): {h_optimo:.2f} pulgadas")
print(f"Área máxima: {area_maxima:.2f} pulgadas cuadradas")
