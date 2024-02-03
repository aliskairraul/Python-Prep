import os
import sys
'''
script Python para anexar a un archivo csv los datos contenidos en el diccionario montañas.
'''

ruta_archivo = './data/clase09_ej3.csv'
montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}


#Asuminedo que todas las listas tienen la misma longitud, y fueron rellenadas con Nan o null 
#para evitar problemas de indices se puede aplicar iteraciones = len(montañas[claves[0]]) 
claves = list(montañas.keys())
iteraciones = len(montañas[claves[0]]) 
indice_ultima_clave = len(claves) -1  

def main():
    '''
    Cuerpo de script:
    '''
    verificar_existe_csv() # Comprueba si el archivo csv existe y de no existir lo crea y anade los encabezados de columnas
    with open(ruta_archivo,'a', encoding='utf-8') as archivo:
        for i in range(iteraciones):
            row = ''
            for j,clave in enumerate(claves): #Para formar la fila debemos añadir de todas las listas el indice i
                row = row +f'{montañas[clave][i]},' if j < indice_ultima_clave  else row + f'{montañas[clave][i]}\n'
            archivo.write(row)

def verificar_existe_csv():
    '''
    Comprueba si el archivo csv existe y de no existir lo crea y añade los encabezados de columnas 
    '''
    if not os.path.exists(ruta_archivo): 
        archivo = open(ruta_archivo,'w')
        encabezado = 'nombre,orden,cordillera,pais,altura\n'
        archivo.write(encabezado)
        archivo.close()


if __name__=='__main__':
    main()