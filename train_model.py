import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Cargar los datos
data = pd.read_excel("Predicciones_Intencion_Emprendedora12.xlsx")

# Seleccionar las características (X) y la variable objetivo (y)
# Asegúrate de incluir las columnas relevantes para tu modelo
X = data.drop(columns=["ProbabilidadIntencionEmprender"])
y = data["ProbabilidadIntencionEmprender"].apply(lambda x: 1 if x > 50 else 0)  # Binario: emprende o no

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Guardar el modelo entrenado
joblib.dump(model, "modelo.pkl")
print("Modelo guardado como 'modelo.pkl'")
