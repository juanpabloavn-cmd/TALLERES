# TALLER DE LABORATORIO
# DEFUZZIFICACIÓN

import numpy as np


# 1. FUNCIÓN PARA CALCULAR EL CENTROIDE

def centroide(x, curva):

    numerador = np.sum(x * curva)
    denominador = np.sum(curva)

    return numerador / denominador


# 2. VALIDACIÓN CON LOS DATOS DEL TALLER ANALÍTICO

x_descuento = np.array([10, 20, 30, 40])

mu_descuento = np.array([0.2, 0.8, 0.8, 0.0])

descuento_final = centroide(
    x_descuento,
    mu_descuento
)

print("VALIDACIÓN DEL DESCUENTO")

print(
    "Descuento exacto:",
    round(descuento_final, 2),
    "%"
)


# 3. SISTEMA DE FRENADO AUTOMÁTICO

# Fuerza de frenado entre 0 y 100 Newtons
x_freno = np.linspace(0, 100, 100)

# Curva de Gauss centrada en 70
centro = 70
sigma = 10

curva_freno = np.exp(
    -((x_freno - centro) ** 2) /
    (2 * sigma ** 2)
)


# 4. DEFUZZIFICACIÓN

fuerza_frenado = centroide(
    x_freno,
    curva_freno
)

print("\nSISTEMA DE FRENADO AUTOMÁTICO")

print(
    "Fuerza de frenado calculada:",
    round(fuerza_frenado, 2),
    "Newtons"
) 