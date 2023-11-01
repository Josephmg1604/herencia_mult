class FiguraGeometrica:
    def __init__(self, ancho:float=None, alto:float=None):
        self._ancho = ancho
        self._alto = alto

    def __str__(self):
        return  f'FiguraGeometrica {self.__dict__.__str__()}'

        @property
        def alto(self):
            return self._alto

        @alto.setter
        def alto(self, alto):
            self._alto = alto

        @property
        def ancho(self):
            return self._ancho

        @ancho.setter
        def ancho(self, ancho):
            self._ancho = ancho

if __name__=='__main__':
    FiguraGeometrica=FiguraGeometrica(4,6)
    print(FiguraGeometrica)