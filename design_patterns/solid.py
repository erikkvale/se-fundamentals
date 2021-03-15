# Single responsibility principle
import math
import html
import json

class Square:
    """A Square type"""
    def __init__(self, length):
        self.length = length

    @property
    def area(self):
        return math.pow(self.length, 2)

    def __repr__(self):
        return f"Square({self.length})"

class Circle:
    """A Circle type"""
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def __repr__(self):
        return f"Circle({self.radius})"


def area_summer(shapes: list) -> float:
    areas = [s.area for s in shapes]
    return sum(areas)


if __name__ == "__main__":
    sq = Square(24.2)
    crc = Circle(23)
    print(sq, crc)
    sum_of_areas = area_summer([sq, crc])
    print(sum_of_areas)


