from sklearn.linear_model import LinearRegression

# Definir las variables independiente (X) y dependiente (y)
X = df[['columna_independiente']]
y = df['columna_dependiente']

# Crear el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Imprimir los coeficientes del modelo
print(f"Intercepto: {modelo.intercept_}")
print(f"Coeficiente: {modelo.coef_[0]}")
