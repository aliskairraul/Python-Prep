import os
import sys
import datetime

'''
A tener en cuenta: El script escribira 4 parametros en un archivo csv:
El parametro 1: sera una marca de tiempo generado automaticamente por el sistema
Los parametros ingresados por el usuario seran:
    2. Temperatura: se guardara en grados centigrados, y se evaluara que este en un rango de -40 a 70 grados
    3. humedad: se guardara en porcentaje, y se evaluara que este en un rango de 0 a 100
    4. lluvia: se guardara en True o False, se evaluara que sea True o False
Los datos seran guardados en el archivo clase09_ej2.csv que se encuentra en la carpeta data.
El script debe verificar si el archivo existe y de no existir lo crea y añade los encabezados de columnas
'''

# Ruta del archivo
ruta_archivo = './data/clase09_ej2.csv'

def main():
    '''
    Cuerpo del script: con sus respectivas Assertions para guardar datos consistentes en el archivo csv
    '''
    try:
        if not len(sys.argv) == 4:
            sys.exit('ERROR: Introdujo una cantidad de argumentos distinta de tres (3)')
        verificar_existe_csv()
        temperatura = sys.argv[1]
        humedad = sys.argv[2]
        lluvia = sys.argv[3].strip().capitalize()
        assert temperatura.isdecimal(), 'El parametro de temperatura no representa un valor numerico'   
        assert float(temperatura) >= -40 and float(temperatura) <= 70, 'rango de temperatura es -40 a 70 grados'
        assert humedad.isdecimal(), 'El parametro de humedad no representa un valor numerico'
        assert float(humedad) >= 0 and float(humedad) <= 100, 'rango de humedad es 0 a 100'
        assert lluvia in ['True', 'False'], 'El parametro de lluvia debe ser True o False'
        with open(ruta_archivo, 'a') as archivo:
            marca_de_tiempo = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            row = f'{marca_de_tiempo},{temperatura},{humedad},{lluvia}\n'
            archivo.write(row)
        print(f'Los datos se han guardado en {ruta_archivo}')
        salida = 'Realizado satisfactoriamente'
    except AssertionError as error:
        print(f'AssertionError: {error}')
        salida = 'Operacion Abortada'
    finally:
        sys.exit(salida)

def verificar_existe_csv():
    '''
    Comprueba si el archivo csv existe y de no existir lo crea y añade los encabezados de columnas 
    '''
    if not os.path.exists(ruta_archivo): 
        archivo = open(ruta_archivo,'w')
        encabezado = 'marca_tirmpo,temperatura,humedad,lluvia\n'
        archivo.write(encabezado)
        archivo.close()




if __name__=='__main__':
    main()

