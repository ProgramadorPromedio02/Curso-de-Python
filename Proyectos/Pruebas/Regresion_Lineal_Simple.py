import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([1, 3, 2, 5, 4])

# Crear el modelo
model = LinearRegression()
model.fit(X, Y)

# Realizar predicciones
Y_pred = model.predict(X)

# Parámetros del modelo
print(f'Intersección (β0): {model.intercept_}')
print(f'Pendiente (β1): {model.coef_[0]}')

# Visualizar los resultados
plt.scatter(X, Y, color='blue')
plt.plot(X, Y_pred, color='red')
plt.xlabel('Variable independiente (X)')
plt.ylabel('Variable dependiente (Y)')
plt.title('Regresión Lineal Simple')
plt.show()

