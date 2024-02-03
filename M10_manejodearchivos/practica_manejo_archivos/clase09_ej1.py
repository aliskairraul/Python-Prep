#Punto 1 de la practica
#Archivo debe recibir al ejecutarse por consola 3 argumentos

import sys

if len(sys.argv) == 4:
    print(f'Usted Introdujo como primer parámetro: {sys.argv[1]}')
    print(f'Usted Introdujo como segundo parámetro: {sys.argv[2]}')
    print(f'Usted Introdujo como tercer parámetro: {sys.argv[3]}')
else:
    print('Usted No intridujo tres(3) parametros y el programa no se ejecutará')
    print('Ejemplo de ejecusion: python clase09_ej1.py parametro1 parametro2 parametro3')
