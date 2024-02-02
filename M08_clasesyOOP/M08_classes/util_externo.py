class UtilExterno():
    def __init__(self,lista):
        self.lista = lista

    def devolver_listas(self):
        lista_primos = self.devolver_lista_primos(self.lista)
        valor_modal,repeticiones = self.valor_modal(self.lista)
        lista_grados = []
        lista_factorial = []
        for elemento in self.lista:
            lista_grados.append(self.conversor_grados(elemento, 'C', 'F'))
            lista_factorial.append(self.factorial(elemento))
        return lista_primos,valor_modal,repeticiones,lista_grados,lista_factorial
        
        
    def verificar_primo_numero(self,n):
        if n in [1,2,3]: return True
        if n%2!=0 and n%3!=0: return True
        return False

    def conversor_grados(self, valor, origen, destino):
            if origen == destino: return valor
            if origen == 'C' and destino == 'F': return (valor * 9 / 5) + 32
            if origen == 'C' and destino == 'K': return (valor + 273.15)
            if origen == 'F' and destino == 'C': return (valor - 32) * 5 / 9
            if origen == 'F' and destino == 'K': return ((valor - 32) * 5 / 9) + 273.15
            if origen == 'K' and destino == 'C': return (valor - 273.15)
            if origen == 'K' and destino == 'F': return ((valor - 273.15) * 9 / 5) + 32

    def devolver_lista_primos(self,lista):
        devuelve_primos = lambda lista:[numero for numero in lista if self.verificar_primo_numero(numero)]
        return devuelve_primos(lista)

    def factorial(self, n):
            fact = 1
            if n > 0:
                for i in range(n, 0, -1):
                    fact = fact * i
            return fact

    def valor_modal(self,lista):
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

        

        