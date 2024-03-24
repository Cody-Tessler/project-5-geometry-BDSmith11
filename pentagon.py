from shape import Shape
import math

class Pentagon(Shape):

    def __init__(self, a):
        self.a = a

    def get_area(self, a):
        return 1/4*math.sqrt(5*(5+2*math.sqrt(5)))*a**2

    def get_perimeter(self, a):
        return 5*a

    def __str__(self):
        return f"Pentagon, a={self.a:0.2f}"

    @classmethod
    def get_area_formula(cls):
        return "1/4*sqrt(5*(5+2*sqrt(5)))*a**2"

    @classmethod
    def get_perimeter_formula(cls):
        return "5*a"
