import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Seleccionar solo las columnas numéricas
df_numeric = df.select_dtypes(include=[float, int])

# 2. Normalización de los Datos
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

# 3. Aplicar PCA
pca = PCA(n_components=2)  # Reducir a 2 componentes principales
df_pca = pca.fit_transform(df_scaled)

# 4. Interpretación de Resultados
print("Varianza explicada por cada componente:", pca.explained_variance_ratio_)
print("Componentes principales:\n", pca.components_)

# 5. Gráfico de los Resultados
plt.figure(figsize=(8, 6))
plt.scatter(df_pca[:, 0], df_pca[:, 1], c='blue', marker='o', edgecolor='k')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Proyección en las dos primeras Componentes Principales')
plt.show()
