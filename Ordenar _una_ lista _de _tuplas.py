import pandas as pd

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel("C:\\Users\\aj\\Downloads\\archivos de clase\\Funcion+Pivot-Alumnos.xlsx")

# Inspeccionar los primeros 5 registros
print(df.head())

# Identificar y manejar valores faltantes
df.fillna(method='ffill', inplace=True)  # Rellenar valores faltantes hacia adelante

# Eliminar filas duplicadas
df.drop_duplicates(inplace=True)
