from color import Color
from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica __init__(self,ancho=lado, alto=lado)
        Color.__init__(self, color=color)

    def calcular_area(self):
        return self._alto * self.ancho

if __name__ == '__main__':
        Cuadrado = Cuadrado(4, 6)
        print(Cuadrado)
        print(cuadrado.mro())