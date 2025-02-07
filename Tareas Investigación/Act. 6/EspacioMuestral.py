import itertools
import pandas as pd
import matplotlib.pyplot as plt

# Definir el espacio muestral
caras_dado = range(1, 21)
espacio_muestral = list(itertools.product(caras_dado, repeat=3))

# Calcular la variable aleatoria X 
valores_X = [sum(resultado) for resultado in espacio_muestral]

# Crear una tabla de frecuencias para X
valores_unicos = sorted(set(valores_X))
frecuencias = [valores_X.count(x) for x in valores_unicos]

# Crear un DataFrame para visualizar mejor los datos
df = pd.DataFrame({'Suma de los Dados (X)': valores_unicos, 'Frecuencia': frecuencias})

# Muestra la tabla
print(df)

# Crear un gráfico de distribución de frecuencias
plt.figure(figsize=(12, 6))
plt.bar(valores_unicos, frecuencias, width=1.0, edgecolor='black', alpha=0.7)
plt.xlabel("Suma de los tres dados (X)")
plt.ylabel("Frecuencia")
plt.title("Distribución de la suma de tres dados de 20 caras")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
