"""
Generador de archivos de datos de estudiantes
Modifica los parámetros en la función main para generar diferentes cantidades
"""

import random
import os

NOMBRES = [
    "María",
    "Carlos",
    "Ana",
    "José",
    "Laura",
    "Pedro",
    "Sofía",
    "Miguel",
    "Valentina",
    "Diego",
    "Camila",
    "Andrés",
    "Isabella",
    "Fernando",
    "Gabriela",
    "Ricardo",
    "Daniela",
    "Jorge",
    "Lucía",
    "Manuel",
]

APELLIDOS = [
    "García",
    "López",
    "Martínez",
    "Rodríguez",
    "Hernández",
    "González",
    "Pérez",
    "Sánchez",
    "Ramírez",
    "Torres",
    "Flores",
    "Rivera",
    "Gómez",
    "Díaz",
    "Morales",
    "Ortiz",
    "Castillo",
    "Jiménez",
    "Vargas",
    "Romero",
]

CARRERAS = [
    "Ingeniería en Sistemas",
    "Medicina",
    "Derecho",
    "Arquitectura",
    "Administración",
    "Psicología",
    "Ingeniería Civil",
    "Economía",
    "Ingeniería Industrial",
    "Comunicación",
]


def generar_nombre():
    nombre = random.choice(NOMBRES)
    apellido1 = random.choice(APELLIDOS)
    apellido2 = random.choice(APELLIDOS)
    return f"{apellido1} {apellido2}, {nombre}"


def generar_estudiante(carne):
    nombre = generar_nombre()
    carrera = random.choice(CARRERAS)
    promedio = round(random.uniform(60, 100), 1)
    return f"{carne}|{nombre}|{carrera}|{promedio}"


def generar_archivos(num_archivos, registros_por_archivo):
    """
    Genera múltiples archivos de estudiantes.

    Args:
        num_archivos: cantidad de archivos a crear
        registros_por_archivo: cantidad de estudiantes por archivo
    """
    os.makedirs("datos", exist_ok=True)

    carne_base = 20210001
    registro_actual = 0

    for num_archivo in range(1, num_archivos + 1):
        nombre_archivo = f"datos/estudiantes_{num_archivo:03d}.txt"

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for _ in range(registros_por_archivo):
                carne = carne_base + registro_actual
                linea = generar_estudiante(carne)
                archivo.write(linea + "\n")
                registro_actual += 1

        print(f"Creado: {nombre_archivo}")

    print(f"\nTotal: {registro_actual} registros")
    print(f"Carnés: {carne_base} - {carne_base + registro_actual - 1}")


# ============================================
# MODIFICA ESTOS VALORES PARA TUS PRUEBAS
# ============================================
generar_archivos(num_archivos=4, registros_por_archivo=20)
