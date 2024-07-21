import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Datos de ejemplo
X = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
y = np.array([1, 2, 3, 4, 5])

# Crear el modelo y ajustarlo
model = LinearRegression()
model.fit(X, y)

# Realizar predicciones
y_pred = model.predict(X)

# Parámetros del modelo
print(f'Intersección (β0): {model.intercept_}')
print(f'Coeficientes (β1, β2): {model.coef_}')

# Visualizar los resultados en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Datos originales
ax.scatter(X[:, 0], X[:, 1], y, color='blue', label='Datos originales')

# Superficie de regresión
X1, X2 = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), 10),
                     np.linspace(X[:, 1].min(), X[:, 1].max(), 10))
Y = model.intercept_ + model.coef_[0] * X1 + model.coef_[1] * X2

ax.plot_surface(X1, X2, Y, color='red', alpha=0.5)

# Etiquetas y título
ax.set_xlabel('Variable independiente 1 (X1)')
ax.set_ylabel('Variable independiente 2 (X2)')
ax.set_zlabel('Variable dependiente (y)')
ax.set_title('Regresión Lineal Múltiple')

plt.show()

