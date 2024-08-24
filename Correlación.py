import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Calcular el coeficiente de correlación de Pearson entre Edad y Número de Accidentes
correlacion = df['edad'].corr(df['accidentes'])
print(f"Coeficiente de Correlación entre Edad y Número de Accidentes: {correlacion}")

# Visualizar la relación con un gráfico de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x='edad', y='accidentes', data=df)
plt.title("Gráfico de Dispersión entre Edad y Número de Accidentes")
plt.xlabel("Edad")
plt.ylabel("Número de Accidentes")
plt.show()
