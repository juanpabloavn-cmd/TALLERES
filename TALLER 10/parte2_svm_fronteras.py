# TALLER DE LABORATORIO
# FRONTERAS NO LINEALES - SVM


import numpy as np
from sklearn.svm import SVC


# 1. DATASET ORIGINAL
# Clase A = 0
# Clase B = 1

X = np.array([
    [2, 2],
    [3, 3],
    [4, 2],
    [6, 6],
    [7, 8],
    [8, 7]
])

Y = np.array([
    0,
    0,
    0,
    1,
    1,
    1
])


# 2. MODELO SVM CON KERNEL LINEAL

modelo_lineal = SVC(
    kernel="linear"
)

modelo_lineal.fit(
    X,
    Y
)


# 3. VECTORES DE SOPORTE

vectores = modelo_lineal.support_vectors_

print("VECTORES DE SOPORTE DEL MODELO LINEAL:")
print(vectores)


# 4. PREDICCIÓN DE UN NUEVO PUNTO

nuevo_punto = np.array([
    [5, 4]
])

prediccion = modelo_lineal.predict(
    nuevo_punto
)

print("\nPREDICCIÓN CON MODELO LINEAL")

print(
    "El punto [5,4] pertenece a la clase:",
    prediccion[0]
)


# 5. AGREGAR PUNTO QUE COMPLICA LA FRONTERA LINEAL

X_nuevo = np.array([
    [2, 2],
    [3, 3],
    [4, 2],
    [6, 6],
    [7, 8],
    [8, 7],
    [5, 5]
])

Y_nuevo = np.array([
    0,
    0,
    0,
    1,
    1,
    1,
    0
])


# 6. ENTRENAR NUEVAMENTE CON KERNEL LINEAL

modelo_lineal_nuevo = SVC(
    kernel="linear"
)

modelo_lineal_nuevo.fit(
    X_nuevo,
    Y_nuevo
)

prediccion_lineal = modelo_lineal_nuevo.predict(
    nuevo_punto
)

print("\nMODELO LINEAL CON EL NUEVO PUNTO")

print(
    "Clase predicha:",
    prediccion_lineal[0]
)

print("Vectores de soporte:")

print(
    modelo_lineal_nuevo.support_vectors_
)


# 7. CAMBIO A KERNEL RBF

modelo_rbf = SVC(
    kernel="rbf"
)

modelo_rbf.fit(
    X_nuevo,
    Y_nuevo
)

prediccion_rbf = modelo_rbf.predict(
    nuevo_punto
)

print("\nMODELO CON KERNEL RBF")

print(
    "Clase predicha:",
    prediccion_rbf[0]
)

print("Vectores de soporte:")

print(
    modelo_rbf.support_vectors_
)