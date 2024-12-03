from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @classmethod
    def info(cls):
        return cls.__name__



class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Circle(Figure):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.PI * self.radius


rect = Rectangle(5, 10)
circle = Circle(7)

print(rect.info(), rect.area())
print(rect.info(), rect.perimeter())
print(circle.info(), circle.area())
print(circle.info(), circle.perimeter())


