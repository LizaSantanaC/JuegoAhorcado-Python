from archivo import Archivo
from juego_ahorcado import JuegoAhoracado

archivo = Archivo()
juego = JuegoAhoracado()
opcion = -1

print("==========BIENBENIDO==========")
while opcion != 0:
    print("\n")
    print("************************")
    print("** MENU DEL JUEGOUEGO **")
    print("************************")
    print("1) Verificar archivo")
    print("2) Llenar archivo con palabras")
    print("3) Borrar archivo")
    print("4) Jugar")
    print("0) SALIR")
    print("-------------------------")
    opcion_string = input("Selecciona una opcion: ")
    if opcion_string.isdigit():
        opcion = int(opcion_string)
    else:
        opcion = -1
    print("\n")
    if opcion == 1:
        palabras_verificadas = archivo.verificar_archivo()
        print("Palabras cargadas: {}".format(palabras_verificadas))
    elif opcion == 2:
        num_palabras = int(input("Numero de palabras a ingresar: "))
        archivo.escribir_palabras(num_palabras)
    elif opcion == 3:
        archivo.borrar_archivo()
    elif opcion == 4:
        if archivo.verificar_archivo() > 0:
            palabras = archivo.palabras
            juego.inicio_ahorcado(juego.elegir_palabra(palabras))
        else:
            print("Archivo vacio, debes ingresar palabras para jugar.")
            num_palabras = int(input("Numero de palabras a ingresar: "))
            archivo.escribir_palabras(num_palabras)
            palabras = archivo.palabras
            juego.inicio_ahorcado(juego.elegir_palabra(palabras))
    elif opcion == 0:
        print("Hasta la proxima")
    else:
        print("Opcion invalida")