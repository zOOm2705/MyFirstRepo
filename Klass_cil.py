import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self._circumference() > other._circumference()

    def __lt__(self, other):
        return self._circumference() < other._circumference()

    def __ge__(self, other):
        return self._circumference() >= other._circumference()

    def __le__(self, other):
        return self._circumference() <= other._circumference()

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        new_radius = self.radius - other.radius
        if new_radius < 0:
            new_radius = 0  # Radius cannot be negative
        return Circle(new_radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __isub__(self, other):
        self.radius -= other.radius
        if self.radius < 0:
            self.radius = 0  # Radius cannot be negative
        return self

    def _circumference(self):
        return 2 * math.pi * self.radius

# Example usage:
circle1 = Circle(5)
circle2 = Circle(10)
print(circle1 == circle2)  # False
print(circle1 < circle2)   # True
circle1 += circle2
print(circle1.radius)      # 15
