import matplotlib.pyplot as plt
import seaborn as sns

# Histograma con línea de densidad
plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.histplot(df['columna'], kde=True)  # Histograma de la columna especificada con densidad
plt.title("Histograma de la columna")  # Título del gráfico
plt.xlabel("Valores de la columna")  # Etiqueta del eje X 
plt.ylabel("Frecuencia")  # Etiqueta del eje Y 
plt.show()  # Mostrar el gráfico

# Gráfico de dispersión
plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.scatterplot(x='columna1', y='columna2', data=df)  # Gráfico de dispersión entre dos columnas
plt.title("Gráfico de dispersión entre columna1 y columna2")  # Título del gráfico
plt.xlabel("Columna 1")  # Etiqueta del eje X 
plt.ylabel("Columna 2")  # Etiqueta del eje Y 
plt.show()  # Mostrar el gráfico

# Gráfico de caja (boxplot)
plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.boxplot(x='columna_categorica', y='columna_numerica', data=df)  # Boxplot comparando categorías y valores numéricos
plt.title("Gráfico de caja")  # Título del gráfico
plt.xlabel("Categorías")  # Etiqueta del eje X 
plt.ylabel("Valores numéricos")  # Etiqueta del eje Y 
plt.show()  # Mostrar el gráfico
