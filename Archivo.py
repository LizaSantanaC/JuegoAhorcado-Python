import os.path as path

class Archivo:
    _ruta_archivo = "palabras.txt"
    def cargar_archivo(self):
        lista_palabras=[]
        archivo = open(self._ruta_archivo)
        for linea in archivo.readlines():
            lista_palabras.append(linea.upper())
        archivo.close()
        return lista_palabras

    def verificar_archivo(self):
        if not path.exists(self._ruta_archivo):
            archivo = open(self._ruta_archivo, "w")



a=Archivo()
a.verificar_archivo()
print(a.cargar_archivo())