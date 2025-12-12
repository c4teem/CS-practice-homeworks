from math import sqrt


class Vector2D:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"x-coordinate: {self.x}, y-coordinate: {self.y}"
    
    def __add__(self, vector):
        new_vector = Vector2D(self.x + vector.x, self.y + vector.y)
        return new_vector
    
    def add2(self, vector):
        self.x += vector.x
        self.y += vector.y

    def __sub__(self, vector):
        new_vector = Vector2D(self.x - vector.x, self.y - vector.y)
        return new_vector
    
    def sub2(self, vector):
        self.x -= vector.x
        self.y -= vector.y
    
    def __mul__(self, vector):
        new_vector = Vector2D(self.x * vector.x, self.y * vector.y)
        return new_vector
    
    def mul2(self, vector):
        self.x *= vector.x
        self.y *= vector.y

    def __len__(self):
        return sqrt(self.x**2 + self.y*2)
    
    def scalar_product(self, vector):
        return self.x * vector.x + self.y * vector.y
    
    def cos(self, vector):
        return (self.scalar_product(vector)) / (self.length() * vector.length())
    
    def __eq__(self, vector):
        return self.x == vector.x and self.y == vector.y
    
x1 = Vector2D()
x2 = Vector2D(2, 3)
x3 = Vector2D(3.33, 3.09078)
x4 = Vector2D(3.33, 2323)
x5 = Vector2D(2, 3)
