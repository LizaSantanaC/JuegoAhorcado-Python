import random
from Archivo import Archivo

class JuegoAhorcado:

    def elegirpalabra(lista_palabras):
        numero_palabras= len(lista_palabras)
        posicion_palabra= random.randint(0, numero_palabras - 1)
        return lista_palabras[posicion_palabra]

    def inicioAhorcado(self):


a=Archivo()
j=JuegoAhorcado()
print(JuegoAhorcado.elegirpalabra(a.cargar_archivo()))