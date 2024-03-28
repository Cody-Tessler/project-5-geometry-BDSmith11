from shape import Shape
import math

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def get_area(self):
        x = math.pi*self.r**2
        return x

    def get_perimeter(self):
        x = 2*math.pi*self.r
        return x

    def __str__(self):
        return f"Circle, r={self.r:0.2f}"

    @classmethod
    def get_area_formula(cls):
        return "pi*r**2"

    @classmethod
    def get_perimeter_formula(cls):
        return "2*pi*r"
