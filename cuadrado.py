from  figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, alto, ancho):
        super() .__init__(alto, ancho)

    def calcular_area(self):
        return self._alto * self.ancho

from color import Color
from figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado , color):
        FiguraGeometrica.__init__(ancho=lado, alto=lado)
        super().__init__(color=color)

    if __name__ == '__main__':
        Cuadrado = Cuadrado(4, 6)
        print(Cuadrado)
