import os.path

class Archivo:
    archivo = 'palabras.txt'
    palabras = []

    def escribir_palabras(self,num_palabras):
        for i in range(num_palabras):
            print("Ingresa la palabra {}".format(i))
            palabra = input()
            self.escribir_palabra(palabra.upper())
        print("Palabras guardadas con exito.")

    def escribir_palabra(self,palabra):
        f = open(self.archivo, 'a')
        f.writelines("\n"+palabra)
        f.close()

    def verificar_archivo(self):
        if self._verificar():
            archivo = open(self.archivo, "r")
            self.palabras = []
            for linea in archivo:
                linea = linea.strip()
                if len(linea) > 0:
                    self.palabras.append(linea)
            return len(self.palabras)
        else:
            f = open(self.archivo, 'wb')
            f.close()
            return 0

    def _verificar(self):
        return os.path.isfile(self.archivo)

    def borrar_archivo(self):
        f = open(self.archivo, 'wb')
        f.writelines("")
        f.close()
        print("Archivo borrado con exito")
        