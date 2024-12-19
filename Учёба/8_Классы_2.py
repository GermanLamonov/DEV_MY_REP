"""Полиморфизм пример в ООП"""
import math


class Shape:
    def calc_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * pow(self.radius, 2)


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calc_area(self):
        return self.height * self.width


shapes = [Circle(3), Rectangle(4, 8), Circle(6.6), Rectangle(13, 18)]
for shape in shapes:
    print(f'Результат = {shape.calc_area():.2f}')
