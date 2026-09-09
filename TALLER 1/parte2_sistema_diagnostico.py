
# 1. MEMORIA DE TRABAJO (Base de Hechos)

servidor_estado = {
    "cpu_uso": 85,
    "memoria_libre": 20,
    "ping_respuesta": 120,
    "temperatura": 85,
    "ventilador_encendido": False
}


# 2. BASE DE REGLAS Y MOTOR DE INFERENCIA

def diagnosticar_servidor(hechos):

    # Regla 1: Estado crítico
    if hechos["temperatura"] > 80 and not hechos["ventilador_encendido"]:
        return "CRÍTICO: Temperatura alta y ventilador apagado."

    # Regla 2: Advertencia por uso de recursos
    elif hechos["cpu_uso"] > 90 and hechos["memoria_libre"] < 15:
        return "ADVERTENCIA: Alto uso de CPU y poca memoria libre."

    # Regla 3: Advertencia por red
    elif hechos["ping_respuesta"] > 200:
        return "ADVERTENCIA: Tiempo de respuesta de red elevado."

    # Regla por defecto
    return "NORMAL: El servidor funciona correctamente."


# 3. EJECUCIÓN

decision = diagnosticar_servidor(servidor_estado)

print("Diagnóstico:", decision)


# 4. PRUEBAS

print("\n--- PRUEBA 1: ESTADO CRÍTICO ---")

servidor_estado["cpu_uso"] = 85
servidor_estado["memoria_libre"] = 20
servidor_estado["ping_respuesta"] = 120
servidor_estado["temperatura"] = 85
servidor_estado["ventilador_encendido"] = False

print("Diagnóstico:", diagnosticar_servidor(servidor_estado))


print("\n--- PRUEBA 2: ADVERTENCIA POR RECURSOS ---")

servidor_estado["cpu_uso"] = 95
servidor_estado["memoria_libre"] = 10
servidor_estado["ping_respuesta"] = 100
servidor_estado["temperatura"] = 65
servidor_estado["ventilador_encendido"] = True

print("Diagnóstico:", diagnosticar_servidor(servidor_estado))


print("\n--- PRUEBA 3: ADVERTENCIA POR RED ---")

servidor_estado["cpu_uso"] = 50
servidor_estado["memoria_libre"] = 50
servidor_estado["ping_respuesta"] = 250
servidor_estado["temperatura"] = 60
servidor_estado["ventilador_encendido"] = True

print("Diagnóstico:", diagnosticar_servidor(servidor_estado))


print("\n--- PRUEBA 4: ESTADO NORMAL ---")

servidor_estado["cpu_uso"] = 40
servidor_estado["memoria_libre"] = 60
servidor_estado["ping_respuesta"] = 50
servidor_estado["temperatura"] = 55
servidor_estado["ventilador_encendido"] = True

print("Diagnóstico:", diagnosticar_servidor(servidor_estado))