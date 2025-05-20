import math

class Figure:
    def dimension(self):
        return 2  # за замовчуванням 2D
    
    def perimeter(self):
        return None
    
    def square(self):
        return None
    
    def volume(self):
        return None

# 2D Фігури

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def square(self):
        # Формула Герона
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def square(self):
        return self.a * self.b

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a  # основа1
        self.b = b  # основа2
        self.c = c  # бічна1
        self.d = d  # бічна2
    
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    
    def square(self):
        # Висоту знайдемо за формулою:
        h = math.sqrt(self.c**2 - (( (self.b - self.a)**2 + self.c**2 - self.d**2 ) / (2*(self.b - self.a)))**2)
        return (self.a + self.b) / 2 * h

class Parallelogram(Figure):
    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def square(self):
        return self.a * self.height

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def square(self):
        return math.pi * self.radius ** 2

# 3D Фігури

class Ball(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def dimension(self):
        return 3
    
    def volume(self):
        return (4/3) * math.pi * self.radius**3

class TriangularPyramid(Triangle):
    def __init__(self, a, height):
        super().__init__(a, a, a)  # правильний трикутник
        self.height = height
    
    def dimension(self):
        return 3
    
    def volume(self):
        base_area = self.square()
        return (1/3) * base_area * self.height

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, height):
        super().__init__(a, b)
        self.height = height
    
    def dimension(self):
        return 3
    
    def volume(self):
        base_area = self.square()
        return (1/3) * base_area * self.height

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    
    def dimension(self):
        return 3
    
    def volume(self):
        return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
    
    def dimension(self):
        return 3
    
    def volume(self):
        return (1/3) * math.pi * self.radius**2 * self.height

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, height):
        super().__init__(a, b, c)
        self.height = height
    
    def dimension(self):
        return 3
    
    def volume(self):
        base_area = self.square()
        return base_area * self.height

def read_figures(filename):
    figures = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            shape = parts[0]
            params = list(map(float, parts[1:]))

            if shape == 'Triangle':
                figures.append(Triangle(*params))
            elif shape == 'Rectangle':
                figures.append(Rectangle(*params))
            elif shape == 'Trapeze':
                figures.append(Trapeze(*params))
            elif shape == 'Parallelogram':
                figures.append(Parallelogram(*params))
            elif shape == 'Circle':
                figures.append(Circle(*params))
            elif shape == 'Ball':
                figures.append(Ball(*params))
            elif shape == 'TriangularPyramid':
                figures.append(TriangularPyramid(*params))
            elif shape == 'QuadrangularPyramid':
                figures.append(QuadrangularPyramid(*params))
            elif shape == 'RectangularParallelepiped':
                figures.append(RectangularParallelepiped(*params))
            elif shape == 'Cone':
                figures.append(Cone(*params))
            elif shape == 'TriangularPrism':
                figures.append(TriangularPrism(*params))

    return figures

def main():
    filename = 'input01.txt'  # змінюй на input02.txt чи input03.txt для тестів
    figures = read_figures(filename)

    # Для площі беремо square() для 2D, volume() для 3D
    def measure(f):
        return f.volume() if f.dimension() == 3 else f.square() or 0

    max_figure = max(figures, key=measure)

    print(f"Фігура з найбільшою мірою (площею або об'ємом): {type(max_figure).__name__}")
    print(f"Міра: {measure(max_figure):.2f}")

if __name__ == '__main__':
    main()
