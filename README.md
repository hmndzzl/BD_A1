# Archivos Secuenciales vs Archivos Indexados

## Objetivo

Implementar y comparar dos métodos de búsqueda en archivos:
- **Búsqueda secuencial**: recorrer todos los registros hasta encontrar el deseado
- **Búsqueda indexada**: usar un índice para acceder directamente al registro

Al finalizar, deberás presentar estadísticas que demuestren la diferencia de rendimiento entre ambos métodos.

---

## Contexto

Tienes un sistema con datos de estudiantes distribuidos en múltiples archivos de texto. Cada archivo representa un "bloque" de registros.

### Formato de los archivos de datos

```
carné|nombre|carrera|promedio
```

Ejemplo (`estudiantes_001.txt`):
```
20210001|López García, Camila|Administración|69.8
20210002|Rivera López, Ana|Medicina|83.6
20210003|García López, María|Arquitectura|69.3
```

### Formato del archivo de índice

```
carné|archivo|posición_en_bytes
```

Ejemplo (`indice.txt`):
```
20210001|estudiantes_001.txt|0
20210002|estudiantes_001.txt|53
20210003|estudiantes_001.txt|95
```

La posición en bytes indica exactamente dónde comienza cada registro dentro del archivo. Esto permite "saltar" directamente a ese punto sin leer las líneas anteriores.

---

## Tu tarea

### Parte 1: Búsqueda secuencial

Implementa una función que busque un estudiante por su carné recorriendo **todos los archivos**, línea por línea, hasta encontrarlo.

Tu función debe:
1. Abrir cada archivo de datos en orden
2. Leer línea por línea hasta encontrar el carné
3. Contar cuántos archivos abrió y cuántas líneas leyó
4. Medir el tiempo que tomó la búsqueda

### Parte 2: Creación del índice

Implementa una función que genere el archivo `indice.txt` a partir de los archivos de datos.

Tu función debe:
1. Recorrer todos los archivos de datos
2. Para cada registro, guardar: `carné|nombre_archivo|posición_en_bytes`
3. La posición se obtiene **antes** de leer cada línea

### Parte 3: Búsqueda indexada

Implementa una función que busque un estudiante usando el índice.

Tu función debe:
1. Buscar el carné en el índice para obtener archivo y posición
2. Abrir únicamente ese archivo
3. Saltar directamente a la posición indicada
4. Leer solo esa línea
5. Medir el tiempo que tomó la búsqueda

### Parte 4: Estadísticas

Ejecuta ambas búsquedas con diferentes carnés y diferentes tamaños de datos. Presenta una tabla comparativa con:

| Métrica | Secuencial | Indexada |
|---------|------------|----------|
| Archivos abiertos | ? | ? |
| Líneas leídas | ? | ? |
| Tiempo (ms) | ? | ? |

---

## Archivos incluidos

```
├── datos/
│   ├── estudiantes_001.txt   # Muestra de datos
│   ├── estudiantes_002.txt
│   └── indice.txt            # Muestra de índice
└── generar_datos.py          # Generador de datos
```

### Uso del generador

```bash
python generar_datos.py
```

Puedes modificar los parámetros en el archivo para generar más o menos datos:

```python
generar_archivos(num_archivos=4, registros_por_archivo=15)
```

Prueba con diferentes tamaños (ejemplo: 10 archivos con 100 registros cada uno) para ver cómo escala cada método.

---

## Snippets de ayuda

### Leer un archivo línea por línea

```python
with open("datos/estudiantes_001.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()  # Eliminar salto de línea
        campos = linea.split("|")
        carne = campos[0]
        nombre = campos[1]
        # ...
```

### Obtener la posición actual en un archivo

```python
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    posicion = archivo.tell()  # Posición actual en bytes
    linea = archivo.readline()
    print(f"La línea comenzaba en el byte {posicion}")
```

### Saltar a una posición específica

```python
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    archivo.seek(738)  # Saltar al byte 738
    linea = archivo.readline()  # Leer desde esa posición
```

### Medir tiempo de ejecución

```python
import time

inicio = time.perf_counter()

# ... código a medir ...

fin = time.perf_counter()
tiempo_ms = (fin - inicio) * 1000
print(f"Tiempo: {tiempo_ms:.4f} ms")
```

### Listar archivos de un directorio

```python
import os

archivos = os.listdir("datos")
# Filtrar solo los archivos de estudiantes
archivos = [f for f in archivos if f.startswith("estudiantes_")]
archivos.sort()  # Ordenar: 001, 002, 003...
```