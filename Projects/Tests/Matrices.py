import numpy as np

# Crear matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Suma
C = A + B
print("Suma:\n", C)

# Resta
D = A - B
print("Resta:\n", D)

# Multiplicación elemento a elemento
E = A * B
print("Multiplicación elemento a elemento:\n", E)

# Producto matricial
F = np.dot(A, B)
# Alternativamente
F = A @ B
print("Producto matricial:\n", F)

# División elemento a elemento
G = A / B
print("División elemento a elemento:\n", G)

