from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Definir las variables X e y
X = df.drop('columna_objetivo', axis=1)
y = df['columna_objetivo']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear y entrenar el modelo de árbol de decisión
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# Predecir y evaluar el modelo
y_pred = modelo.predict(X_test)
print(f"Precisión del modelo: {accuracy_score(y_test, y_pred)}")
