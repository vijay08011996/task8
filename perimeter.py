import math

class Circle:
    def __init__(self, radius_list):
        self.__pi = 3.141  # Private variable for pi
        self.radius_list = radius_list

    def area(self):
        areas = [self.__pi * (r ** 2) for r in self.radius_list]
        return areas

    def perimeter(self):
        perimeters = [2 * self.__pi * r for r in self.radius_list]
        return perimeters

# Example usage:
radius_values = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_values)
areas = circle_instance.area()
perimeters = circle_instance.perimeter()

print("Areas of circles with given radii:", areas)
print("Perimeters of circles with given radii:", perimeters)
