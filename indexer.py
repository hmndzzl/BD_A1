import os
import random


# ============================================
# GENERAR ARCHIVOS DE PRUEBA
# ============================================


"""def generar_archivos_prueba():
    os.makedirs(CARPETA_DATOS, exist_ok=True)

    carnet = 260001

    for i in range(1, TOTAL_ARCHIVOS + 1):
        nombre_archivo = f"estudiantes_{i:03}.txt"
        ruta = os.path.join(CARPETA_DATOS, nombre_archivo)

        with open(ruta, "w", encoding="utf-8") as f:
            for j in range(REGISTROS_POR_ARCHIVO):
                nombre = random.choice(NOMBRES)
                apellido = random.choice(APELLIDOS)
                carrera = random.choice(CARRERAS)

                registro = f"{carnet}-{nombre} {apellido}-{carrera}|"
                f.write(registro)

                carnet += 1

    print("✔ Archivos de prueba generados")"""


# ============================================
# GENERAR ÍNDICE
# ============================================


def generar_indice(carpeta, archivo_indice):
    with open(archivo_indice, "w", encoding="utf-8") as idx:

        for archivo in sorted(os.listdir(carpeta)):
            ruta = os.path.join(carpeta, archivo)

            if not archivo.endswith(".txt"):
                continue

            with open(ruta, "r", encoding="utf-8") as f:
                byte_offset = 0
                buffer = ""

                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break

                    buffer += chunk

                    while "|" in buffer:
                        registro, buffer = buffer.split("|", 1)

                        if registro.strip() == "":
                            continue

                        numero_carnet = registro.split("-")[0]
                        idx.write(f"{numero_carnet}|{archivo}|{byte_offset}\n")

                        byte_offset += len(registro.encode("utf-8")) + 1

                byte_offset += len(buffer.encode("utf-8"))

    print("✔ Índice generado correctamente")


# ============================================
# BUSCAR ESTUDIANTE USANDO EL ÍNDICE
# ============================================


def buscar_estudiante(numero_carnet, archivo_indice, carpeta):
    with open(archivo_indice, "r", encoding="utf-8") as idx:
        for linea in idx:
            carnet, archivo, offset = linea.strip().split("|")

            if carnet == numero_carnet:
                ruta = os.path.join(carpeta, archivo)

                with open(ruta, "r", encoding="utf-8") as f:
                    f.seek(int(offset))
                    registro = ""

                    while True:
                        char = f.read(1)
                        if char == "|" or char == "":
                            break
                        registro += char

                # Se concatena el nombre del archivo al string
                return f"{registro}|{archivo}"

    return None


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

CARPETA_DATOS = "datos"
ARCHIVO_INDICE = "indice_estudiantes.txt"
REGISTROS_POR_ARCHIVO = 1000
TOTAL_ARCHIVOS = 5

NOMBRES = ["Ana", "Luis", "María", "Juan", "Carlos", "Sofía", "Pedro", "Laura"]
APELLIDOS = ["Pérez", "Gómez", "López", "Martínez", "Hernández", "Ramírez"]
CARRERAS = ["Ingeniería", "Medicina", "Derecho", "Arquitectura", "Economía"]

# generar_archivos_prueba()

# generar_indice(CARPETA_DATOS, ARCHIVO_INDICE)

# Prueba de búsqueda
carnet_prueba = "260001"
resultado = buscar_estudiante(carnet_prueba, ARCHIVO_INDICE, CARPETA_DATOS)

print("Resultado de búsqueda:")
print(resultado)
