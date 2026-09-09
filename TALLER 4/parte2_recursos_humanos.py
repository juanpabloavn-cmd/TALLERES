# TALLER DE LABORATORIO
# MOTOR LÓGICO DE RECURSOS HUMANOS


# 1. GRADOS DE MEMBRESÍA DEL EMPLEADO

grados = {
    "desempeno_pobre": 0.1,
    "desempeno_promedio": 0.5,
    "desempeno_excelente": 0.85,
    "antiguedad_corta": 0.2,
    "antiguedad_larga": 0.6
}


# 2. EVALUACIÓN DE REGLAS MANDANI

def evaluar_bono(grados):

    # R1:
    # SI Desempeño es Pobre O Antigüedad es Corta
    # ENTONCES Bono = Bajo

    activacion_r1 = max(
        grados["desempeno_pobre"],
        grados["antiguedad_corta"]
    )


    # R2:
    # SI Desempeño es Promedio
    # ENTONCES Bono = Medio

    activacion_r2 = grados["desempeno_promedio"]


    # R3:
    # SI Desempeño es Excelente Y Antigüedad es Larga
    # ENTONCES Bono = Alto

    activacion_r3 = min(
        grados["desempeno_excelente"],
        grados["antiguedad_larga"]
    )


    return {
        "Bono Bajo": activacion_r1,
        "Bono Medio": activacion_r2,
        "Bono Alto": activacion_r3
    }


# 3. EJECUCIÓN

resultado = evaluar_bono(grados)

print("Niveles de activación:")
print(resultado)


# 4. AGREGACIÓN MANDANI

# Dos reglas diferentes concluyen Bono Alto
fuerza_alto_1 = 0.4
fuerza_alto_2 = 0.7

fuerza_final_alto = max(
    fuerza_alto_1,
    fuerza_alto_2
)

print("\nAgregación para Bono Alto:")
print("Fuerza de la primera regla:", fuerza_alto_1)
print("Fuerza de la segunda regla:", fuerza_alto_2)
print("Fuerza final de Bono Alto:", fuerza_final_alto)