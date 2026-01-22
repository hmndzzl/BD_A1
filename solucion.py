# Aquí vamos a ir trabajando las soluciones 

import os
import time
import glob

CARPETA_DATOS = "datos"
ARCHIVO_INDICE = "indice.txt"

# obtener la ruta del directorio actual para los archivos 
ruta = os.path.dirname(os.path.abspath(__file__))

#---------------------------------------------

#funcion para realizar la busqueda secuencial
def secuencial(carnet_estudiante, documentos):
    # variables
    
    archivos_leidos = 0
    lineas_leidas = 0
    estudiante_correspondiente = None
    tiempo_inicio = time.perf_counter()

    #bucle para recorrer los documentos
    for doc in documentos:
        # se abre el documento con open en modo lectura con r y se utiliza utf-8 para caracteres especiales
        try:
            with open(doc, 'r', encoding = 'utf-8') as archivo_abierto:
                archivos_leidos += 1

                # se recorre cada linea del archivo y se van contando las lineas leidas
                for linea in archivo_abierto:
                    lineas_leidas += 1
                    linea = linea.strip() # eliminar espacios en blanco al inicio y final para evitar errores

                    if not linea:
                        continue

                    #se especifica el formato del archivo
                    carnet, nombre, carrera, promedio = linea.split('|') 
                    #se compara el carnet del estudiante con el carnet solicitado
                    if carnet == carnet_estudiante:
                        estudiante_correspondiente = {"carnet": carnet, "nombre": nombre, "carrera": carrera, "promedio": float(promedio), "documento": doc}

                        #si hay exito se toma el tiempo final y se calcula el tiempo de ejecucion de la busqueda 
                        tiempo_final = time.perf_counter()
                        tiempo_ejecucion = tiempo_final - tiempo_inicio

                        # se retornan los valores correspondientes
                        return estudiante_correspondiente, archivos_leidos, lineas_leidas, tiempo_ejecucion
                    
        except FileNotFoundError:
            print(f"El archivo {doc} no se encontro")
    #si no hay exito se toma el tiempo final y se calcula el tiempo de ejecucion de la busqueda final
    tiempo_final = time.perf_counter()
    tiempo_ejecucion = tiempo_final - tiempo_inicio

    # se retornan los valores correspondientes
    return None, archivos_leidos, lineas_leidas, tiempo_ejecucion

#---------------------------------------------

# Función para la generación del index.txt
def generar_indice(carpeta, archivo_indice):
    with open(archivo_indice, "w", encoding="utf-8") as idx:

        for archivo in sorted(os.listdir(carpeta)):
            ruta = os.path.join(carpeta, archivo)

            if not archivo.endswith(".txt") or archivo == archivo_indice:
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


#---------------------------------------------------------------------------------------------

# se especifican los archivos a revisar de forma automática y el carnet a buscar
archivos_a_revisar = sorted(glob.glob(os.path.join(ruta, "datos", "estudiantes_*.txt")))

carnet_buscado = "20210042"

# ejecucion de la busqueda secuencial
resultado, archivos_recorridos, lineas_recorridas, tiempo_total = secuencial(carnet_buscado, archivos_a_revisar)

# Generar el archivo con los índices
generar_indice(CARPETA_DATOS, ARCHIVO_INDICE)

# resultados de la busqueda
if resultado:
    print("ruta del archivo: " + resultado['documento'])    
    print("Estudiante correspondiente al carnet buscado:")
    print(resultado)
    print(f"Numero de archivos abiertos: {archivos_recorridos}")
    print(f"Total de lineas leidas: {lineas_recorridas}")
    print(f"Tiempo total de la busqueda: {tiempo_total:.6f} s")
else:
    print("Estudiante no encontrado")
