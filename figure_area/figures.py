class Shape:
    def __init__(self) -> None:
        pass

class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius
    
    def area(self) -> float:
        return round(3.14 * (self.radius ** 2), 2)


class Triangle(Shape):
    def __init__(self, side1: int, side2: int, side3: int) -> None:
        self.a, self.b, self.c = side1, side2, side3
        self.p = (self.a + self.b + self.c) / 2
    
    def area(self) -> float:
        S = (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5
        return round(S, 2)
    
    def is_rectangular(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        return "Прямоугольный" if sides[0]**2 + sides[1]**2 == sides[2]**2 else "Не прямоугольный"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return round(self.width * self.height, 2)
