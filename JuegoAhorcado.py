import random
from Archivo import Archivo

class JuegoAhorcado:
    # Variables
    palabraSecreta = ""
    palabraM = []
    palabraV = []
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]

    #Método elegir elegirPalabra
    def elegirPalabra(lista_palabras):
        numero_palabras= len(lista_palabras)
        posicion_palabra= random.randint(0, numero_palabras - 1)
        return lista_palabras[posicion_palabra]

#Clase que contendrá los método para cargar y agregar las palabras
class archivoPalabras:

    #Método para cargar palabra
    def cargarPalabra(self):
        Archivo= open("palabras.txt", "r+")
        numeroLinea= 0
        numeroRandom= 0
        lista= Archivo.readline()
        numeroRandom= int(random() * len(lista) + 1)
        for linea in lista:
            numeroLinea += 1
            if(numeroLinea == numeroRandom):
                palabra= ""
                palabra= linea
                palabraSecreta= palabra.upper()
                print("La palabra tiene " + str(len(palabraSecreta)) + "letras")
                if(numeroRandom == 1):
                    for i in range(len(palabraSecreta) - 1):
                        self.palabraM("_ ")
                        print(self.palabraM)
                else:
                    for i in range(len(palabraSecreta)):
                        self.palabraM.append("_ ")
                        print(self.palabraM)
                        Archivo.close()

#Clase para validar las palabras
class validacionesPalabra:

    # Método para validar los caracteres de las palabras
    def validarCaracter(self, caracter):
        caracter= 0
        for i in range(len(self.abecedario)):
            if(self.abecedario[i])
    #Método para validar las palabras
    def validarPalabra(self, palabra):
        comparacion= ""
        for i in range(len(palabra)):
            comparacion= palabra[i : (i + 1)]
            if(self.)


a=Archivo()
j=JuegoAhorcado()
print(JuegoAhorcado.elegirPalabra(a.cargar_archivo()))