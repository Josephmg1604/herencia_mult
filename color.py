from  figura_geometrica import FiguraGeometrica

class Color:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color

    def __str__(self):
        return f"Color: {self._color}"
    @p

# Ejemplo de uso:
mi_color = Color("Azul")
print(mi_color)  # Output: Color: Azul

# Accediendo y modificando el color usando getters y setters
print(mi_color.get_color())  # Output: Azul
mi_color.set_color("Verde")
print(mi_color.get_color())  # Output: Verde
print(mi_color)  # Output: Color: Verde
