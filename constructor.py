import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = [math.pi * (r ** 2) for r in self.radius_list]
        return areas

# Example usage:
radius_values = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_values)
areas = circle_instance.calculate_area()
print("Areas of circles with given radii:", areas)
