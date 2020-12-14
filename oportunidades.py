class Oportunidades:
    oportunidades = 10

    def reducir_oportunidades(self):
        self.oportunidades = self.oportunidades - 1
        return self.oportunidades

    def aumentar_oportunidades(self):
        self.oportunidades = self.oportunidades + 1
        return self.oportunidades

    def reiniciar(self):
        self.oportunidades = 10
