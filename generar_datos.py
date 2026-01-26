"""
Generador de archivos de datos de estudiantes
Modifica los parámetros en la función main para generar diferentes cantidades
"""

import random
import os

CARPETA_DATOS = "datos"
ARCHIVO_INDICE = os.path.join(CARPETA_DATOS, "indice.txt")

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



# Función para la generación del index.txt
def generar_indice(carpeta, archivo_indice):
    with open(archivo_indice, "w", encoding="utf-8") as idx:

        for archivo in sorted(os.listdir(carpeta)):
            ruta = os.path.join(carpeta, archivo)

            if not archivo.endswith(".txt") or archivo == os.path.basename(archivo_indice):
                continue

            with open(ruta, "rb") as f:
                byte_offset = 0
                for line in f:
                    #offset acutal
                    current_line_offset = byte_offset
                    # offset siguiente linea
                    byte_offset += len(line)
                    
                    contenido = line.decode("utf-8").strip()
                    if not contenido:
                        continue

                    # formato carné|nombre|carrera|promedio
                    partes = contenido.split("|")
                    if partes:
                        numero_carnet = partes[0]
                        idx.write(f"{numero_carnet}|{archivo}|{current_line_offset}\n") # Queremos carné|archivo|posición_en_bytes

    print("Índice generado correctamente")


# ============================================
# MODIFICA ESTOS VALORES PARA TUS PRUEBAS
# ============================================
generar_archivos(num_archivos=8, registros_por_archivo=35)

#Si generamos más archivos y luego queremos generar menos (ej. generamos 10 y ahora queremos probar con 4)
# debemos eliminar los archivos que sobran manualmente

# Generar el archivo con los índices
generar_indice(CARPETA_DATOS, ARCHIVO_INDICE)
