from shape import Shape
import math

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        x = self.a*self.b
        return f'{x:0.2f}'

    def get_perimeter(self):
        x = 2*(self.a + self.b)
        return f'{x:0.2f}'

    def __str__(self):
        return f"Rectangle, a={self.a:0.2f}, b={self.b:0.2f}"

    @classmethod
    def get_area_formula(cls):
        return "a*b"

    @classmethod
    def get_perimeter_formula(cls):
        return "2*(a + b)"
