import pandas as pd

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel("C:\\Users\\aj\\Downloads\\archivos de clase\\Funcion+Pivot-Alumnos.xlsx")

# Calcular estadísticas descriptivas
descripcion = df.describe()
print("Estadísticas Descriptivas:")
print(descripcion)

# Calcular la mediana y la moda de una columna específica
DIASEMANA = 'nombre_de_columna'

mediana = df[DIASEMANA].median()
moda = df[
    DIASEMANA
].mode()[0]

print(f"Mediana de la columna {DIASEMANA}: {mediana}")
print(f"Moda de la columna {DIASEMANA}: {moda}")
