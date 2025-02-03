import matplotlib.pyplot as plt
import pandas as pd

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv('Datos_practica.csv', sep=';')

# Crear un histograma de la columna 'Cu'
plt.figure(figsize=(10, 6))
plt.hist(df['Cu'], bins=10, edgecolor='k', alpha=0.7)
plt.xlabel('Cu (Copper)')
plt.ylabel('Frequency')
plt.title('Histograma de Concentración de Cobre (Cu)')
plt.grid(True)

# Guardar el histograma como una imagen
plt.savefig('histograma_cu.png')

