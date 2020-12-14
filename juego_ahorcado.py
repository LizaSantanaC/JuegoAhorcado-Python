from random import random, choice
from oportunidades import Oportunidades


class JuegoAhoracado:

    oportunidades = Oportunidades()
    _letras_disponibles = "abcdefghijklmnopqrstuvwxyz"

    def inicio_ahorcado(self, palabra):
        palabra = palabra.lower()
        print("********************************")
        print("Estoy pensado en una palabra de {} letras".format(len(palabra)))
        print("")

        letras_ingresadas = []

        while self.oportunidades.oportunidades > 0:
            print("-------------------------------------------------")
            print("Te quedan {} oportunidades para adivinar.".format(self.oportunidades.oportunidades))
            print("Letras disponibles: "+ self.obtener_letras_disponibles(letras_ingresadas))
            letra_ingresada = self.pedir_letra(letras_ingresadas)
            letras_ingresadas.append(letra_ingresada)
            if letra_ingresada not in palabra:
                self.oportunidades.reducir_oportunidades()
                print("¡Bien hecho!")
            else:
                print("Oops! Esa letra no está en la palabra secreta")

            print("PALABRA SECRETA: "+self.obtener_palabra_adivinada(palabra,letras_ingresadas) + "\n")

            if self.se_adivino_palabra(palabra,letras_ingresadas):
                print("**************************************************")
                print("** FELICIDADES HAS ADIVINADO LA PALABRA SECRETA **")
                print("**************************************************")
                return

            if self.oportunidades.oportunidades == 0:
                print("**********GAME OVER***************")
                print("La palabra secreta era: "+palabra.upper())
                print("Suerte para la proxima")


    def elegir_palabra(self,listaPalabras):
        return choice(listaPalabras)

    def se_adivino_palabra(self, palabra_secreta,letras_ingresadas):
        num_letras = 0
        for letra in palabra_secreta:
            if letra in letras_ingresadas:
                num_letras = num_letras + 1

        return len(palabra_secreta) == num_letras

    def obtener_palabra_adivinada(self,palabra_secreta,letras_ingresadas):
        palabra_guiones = ""
        for caracter in palabra_secreta:
            if caracter in letras_ingresadas:
                palabra_guiones = palabra_guiones + " " +caracter
            else:
                palabra_guiones = palabra_guiones + " _ "
        return palabra_guiones.upper()

    def obtener_letras_disponibles(self,letras_ingresadas):
        if len(letras_ingresadas) == 0:
            return self._letras_disponibles

        letras = self._letras_disponibles
        for letra in letras_ingresadas:
            letras = letras.replace(letra, " _ ")
        return  letras

    def pedir_letra(self,algunaLetra):
        while True:
            letra = input("Por favor ingresa una letra: ")
            letra = letra.lower()
            if len(letra) != 1:
                print('Introduce una sola letra.')
            elif letra in algunaLetra:
                print('Ya has elegido esa letra, elige otra.')
            elif letra not in 'abcdefghijklmnopqrstuvwxyz':
                print('Elije una letra.')
            else:
                return letra