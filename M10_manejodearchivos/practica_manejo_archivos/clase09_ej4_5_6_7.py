import sys
import os
import shutil

'''
    Aspectos a tener en cuenta:
    1. 'os.path.getsize()' devuelve el tamaño de un archivo en disco en bytes.
    2. 1kb = 1024 bytes y 1mb = 1048576 bytes
    3. Dado que el archivo devuelve un tamaño en bytes que no llega a 400 bytes el resultado
       expresado en MB va a ser poco legible. En este caso visualizaré el tamaño en kb
'''

directorio_actual = os.getcwd()

# Punto 4 del Homework --> Obtener tamaño del csv que guardo los datos de las montañas
tamanho = round(os.path.getsize('./data/clase09_ej3.csv')/1024,2)
print('='*50)
print('PUNTO 4 DEL HOMEWORK:')
print(f'El tamaño del archivo es {tamanho} kb')


# Punto 5 del Homework --> Crear una carpeta llamada clase09_montañas_altas
print('='*50)
print('PUNTO 5 DEL HOMEWORK:')
os.makedirs('./data/clase09_montañas_altas')
print(os.listdir('./data'))

# Punto 6 del Homework --> Copiar el archivo clase09_ej3.scv en la carpeta del punto anterior
# dir_ar = directorio_actual+'\data\clase09_ej3.scv' --> #problema con windows y su \ para separar directorios, Python interpreta \ dentro de comillas como un salto
dir_ar = "C:/Users/alisk/Documents/henry/Python-Prep/M10_manejodearchivos/practica_manejo_archivos/data/clase09_ej3.csv"
destino = directorio_actual+'\data\clase09_montañas_altas'
shutil.copy(dir_ar, destino)
print('='*50)
print('PUNTO 6 DEL HOMEWORK:')


# Punto 7 del Homework --> Listar el contenido de la carpeta clase09_montañas_altas
print('='*50)
print('PUNTO 7 DEL HOMEWORK:')
print(os.listdir('./data/clase09_montañas_altas'))








# El comando para copiar un archivo de una carpeta a otra usando la librería `os` de Python es `shutil.copy()`. Su sintaxis es la siguiente:

# ```
# shutil.copy(src, dst)
# ```

# Donde:

# * `src` es la ruta del archivo que se quiere copiar.
# * `dst` es la ruta del destino donde se quiere copiar el archivo.

# Por ejemplo, para copiar el archivo `archivo.txt` de la carpeta `carpeta1` a la carpeta `carpeta2`, se usaría el siguiente código:

# ```python
# import shutil

# ruta_origen = "carpeta1/archivo.txt"
# ruta_destino = "carpeta2/archivo.txt"

# shutil.copy(ruta_origen, ruta_destino)
# ```

# También se puede usar la función `shutil.copytree()` para copiar una carpeta entera y todo su contenido a otra carpeta. Su sintaxis es la siguiente:

# ```
# shutil.copytree(src, dst)
# ```

# Donde:

# * `src` es la ruta de la carpeta que se quiere copiar.
# * `dst` es la ruta de la carpeta de destino donde se quiere copiar la carpeta.

# Por ejemplo, para copiar la carpeta `carpeta1` y todo su contenido a la carpeta `carpeta2`, se usaría el siguiente código:

# ```python
# import shutil

# ruta_origen = "carpeta1"
# ruta_destino = "carpeta2"

# shutil.copytree(ruta_origen, ruta_destino)
# ```

# Ten en cuenta que la función `shutil.copytree()` copiará todos los archivos y subcarpetas de la carpeta origen a la carpeta destino. Si la carpeta destino ya existe, se sobrescribirá su contenido.



# import os
# import shutil

# # Ruta del archivo de origen
# src = "/home/usuario/Documentos/archivo.txt"

# # Ruta del archivo o directorio de destino
# dst = "/home/usuario/Escritorio/copia.txt"

# # Copiar el archivo usando shutil.copy
# shutil.copy(src, dst)

# # Copiar el archivo usando shutil.copyfile
# shutil.copyfile(src, dst)






# **sys.getsizeof()**

# * **Uso:** `sys.getsizeof(objeto)`
# * **Descripción:** Devuelve el tamaño de un objeto en bytes. El tamaño de un objeto es la cantidad de memoria que ocupa en el proceso.
# * **Ventajas:**
#     * Puede utilizarse para cualquier tipo de objeto, no sólo para archivos.
#     * Es más rápido que `os.path.getsize()`.
# * **Desventajas:**
#     * No devuelve el tamaño del objeto en el disco, sino el tamaño en la memoria.
#     * Puede devolver un tamaño diferente para el mismo objeto, dependiendo de cómo se haya creado.

# **os.path.getsize()**

# * **Uso:** `os.path.getsize(ruta)`
# * **Descripción:** Devuelve el tamaño de un archivo en bytes. El tamaño de un archivo es la cantidad de espacio que ocupa en el disco.
# * **Ventajas:**
#     * Devuelve el tamaño del archivo en el disco, no el tamaño en la memoria.
#     * Es más preciso que `sys.getsizeof()`.
# * **Desventajas:**
#     * Sólo puede utilizarse para archivos.
#     * Es más lento que `sys.getsizeof()`.

# En general, `sys.getsizeof()` es más útil para determinar el tamaño de un objeto en la memoria, mientras que `os.path.getsize()` es más útil para determinar el tamaño de un archivo en el disco.

# Aquí hay un ejemplo de cómo se pueden utilizar estas dos funciones:

# ```python
# import sys
# import os

# # Obtener el tamaño de un objeto en la memoria
# objeto = [1, 2, 3, 4, 5]
# tamaño_objeto = sys.getsizeof(objeto)
# print("Tamaño del objeto:", tamaño_objeto)

# # Obtener el tamaño de un archivo en el disco
# ruta = "archivo.txt"
# tamaño_archivo = os.path.getsize(ruta)
# print("Tamaño del archivo:", tamaño_archivo)
# ```

# Este código imprimirá lo siguiente:

# ```
# Tamaño del objeto: 88
# Tamaño del archivo: 1024
# ```

# Como se puede ver, el tamaño del objeto en la memoria es mucho menor que el tamaño del archivo en el disco. Esto se debe a que el objeto sólo contiene los datos, mientras que el archivo también contiene información adicional, como los metadatos.