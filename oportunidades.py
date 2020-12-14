class Oportunidades:
    _oṕortunidades = 10

    def disminuir_oportunidad(self):
        self._oṕortunidades = self._oṕortunidades - 1
        return self._oṕortunidades

    def reiniciar_oportunidades(self):
        self._oṕortunidades= 10

    def obtener_oportunidade(self):
        return self._oṕortunidades
