class InstanciaUtilidadException(Exception):
    def __init__(self, message):
        self.message = message

class UtilExterno():
    def __init__(self,lista):
        if type(lista) != list: 
            self.lista = []
            raise ValueError('Se esperaba una lista para Instanciar la Clase')
        else:
            self.lista = lista


    def devolver_listas(self):
        '''
        devolver_listas: Metodo encargado de retornar las listas de los métodos, aplicando los valores 
                         de la lista con que se instancio la clase.
        '''
        lista_primos = self.devolver_lista_primos(self.lista)
        valor_modal,repeticiones = self.valor_modal(self.lista)
        lista_grados = []
        lista_factorial = []
        for elemento in self.lista:
            lista_grados.append(self.conversor_grados(elemento, 'C', 'F'))
            lista_factorial.append(self.factorial(elemento))
        return lista_primos,valor_modal,repeticiones,lista_grados,lista_factorial
        
        
    def verificar_primo_numero(self,n):
        '''
        verificar_primo_numero: Se encarga de verificar si un numero es primo
                                retornando True o False
        Parametros: n: debe ser un del tipo int y positivo
        '''
        assert type(n) == int and n > 0, 'En el metodo verificar_primo_numero el parametro n debe ser un entero'
        assert n > 0,  'En el metodo verificar_primo_numero el parametro n debe ser positivo'
        try:
            if n in [1,2,3]: return True
            if n%2!=0 and n%3!=0: return True
            return False
        except AssertionError as e: return e

    def lista_grados(self,lista,origen,destino):
        '''
        lista_grados: Se encarga de retornar la lista de valores equivalentes segun la escale de origen y destino
                      Se apoya en self.conversor_grados para la mayoria de su implementacion. encargandose 
                      unicamente de validar que sea de Type list el parametro lista y todo lo demas se valida y calcula
                      en self.conversor_grados
        Parametros: lista: del tipo list
        '''
        lista_grados = lambda lista: [self.conversor_grados(elemento,origen,destino) for elemento in lista]
        return(lista_grados(lista))


    def conversor_grados(self, valor, origen, destino):
            '''
            conversor_grados: Se encarga de retornar la equivalencia de un valor entre distintas escalas de Temperatura
            Parametros: valor: debe ser un del tipo int
                        origen, destino: debe ser un del tipo string (C, F o K)
            '''
            assert type(valor) == float or type(valor) == int, 'En el metodo conversor_grados valor debe ser un numero'
            assert type(origen) == str and type(destino) == str, 'En el metodo conversor_grados origen y destino deben ser strings'
            assert origen in ['C', 'F', 'K'] and destino in ['C', 'F', 'K'], 'origen y destino deben ser C, F o K'
            try:
                if origen == destino: return valor
                if origen == 'C' and destino == 'F': return (valor * 9 / 5) + 32
                if origen == 'C' and destino == 'K': return (valor + 273.15)
                if origen == 'F' and destino == 'C': return (valor - 32) * 5 / 9
                if origen == 'F' and destino == 'K': return ((valor - 32) * 5 / 9) + 273.15
                if origen == 'K' and destino == 'C': return (valor - 273.15)
                if origen == 'K' and destino == 'F': return ((valor - 273.15) * 9 / 5) + 32
            except AssertionError as e: return e

    def devolver_lista_primos(self,lista):
        '''
        devolver_lista_primos: Se encarga de retornar unicamente los valores primos de la lista recibida.
        Parametros: lista: debe ser una lista de enteros positivos                      
        '''
        assert type(lista) == list, 'En el metodo devolver_lista_primos el parametro lista debe ser una lista'
        try:
            devuelve_primos = lambda lista:[numero for numero in lista if self.verificar_primo_numero(numero)]
            return devuelve_primos(lista)
        except AssertionError as e: return e

    def devolver_son_primos(self,lista):
        '''
        devolver_son_primos: Recibe una lista de enteros positivos y devulve otra lista que indica
                             en cada posicion True o False segun sea o no primo el elemento
                             este metodo se creo para respesta especifica del Modulo 9 del Homework Henry
        Parametros: lista: debe ser una lista de enteros positivos
        '''
        assert type(lista) == list, 'En el metodo devolver_son_primos el parametro lista debe ser una lista'
        try:
            devuelve_son_primos = lambda lista:[self.verificar_primo_numero(numero) for numero in lista]
            return devuelve_son_primos(lista)
        except AssertionError as e: return e

    def lista_factorial(self,lista):
        '''
        lista_factorial: Se encarga de retornar el factorial de cada elemento de la lista
                         apoyado en el metodo self.factorial
        '''
        assert type(lista) == list, 'En el metodo devolver_son_primos el parametro lista debe ser una lista'
        lista_factorial = lambda lista:[self.factorial(elemento) for elemento in lista]
        return lista_factorial(lista)



    def factorial(self, n):
        '''
        factorial: Se encarga de retornar el factorial de un numero entero positivo
        Parametro: n: debe ser un entero positivo
        '''
        assert type(n) == int and n > 0, 'En el metodo factorial el parametro n debe ser un entero'
        assert n > 0,  'En el metodo factorial el parametro n debe ser positivo'
        try:
            fact = 1
            if n > 0:
                for i in range(n, 0, -1):
                    fact = fact * i
            return fact
        except AssertionError as e: return e

    def valor_modal(self,lista):
        '''
        valor_modal: Se encarga de retornar el valor modal de una lista
        Parametro: lista: debe ser una lista
        '''
        assert type(lista) == list, 'En el metodo valor_modal el parametro lista debe ser una lista'
        try:
            diccionario ={}
            for elemento in lista:
                if elemento in diccionario:
                    diccionario[elemento] += 1
                else:
                    diccionario[elemento] = 1
            valor_modal = 0
            veces = 0
            for clave in diccionario:
                if diccionario[clave] > veces:
                    veces = diccionario[clave]
                    valor_modal = clave
            return valor_modal,veces
        except AssertionError as e: return e

        

        