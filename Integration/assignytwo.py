
import math

def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return 2 * (width + height)

def circle_area(radius):
    return math.pi * radius**2

def circle_circumference(radius):
    return 2 * math.pi * radius

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
