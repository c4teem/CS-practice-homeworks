class Matrix2x2:

    def __init__(self, x11, x12, x21, x22):
        self.x11 = x11
        self.x12 = x12
        self.x21 = x21
        self.x22 = x22

    def __str__(self):
        s1 = f"Matrix = |{self.x11} {self.x12}|"
        s2 = f"\n         |{self.x21} {self.x22}|"
        length1 = len(s1)
        length2 = len(s2)

        if length1 < length2:
            l = length2 - length1
            s1 = f"Matrix = |{self.x11}{" " * l}{self.x12}|"
            return s1 + s2
        elif length1 > length2:
            l = length1 - length2 + 1
            s2 = f"\n         |{self.x21} {" " * l}{self.x22}|"
            return s1 + s2
        else:
            return s1 + s2

    def __add__(self, other):
        if isinstance(other, Matrix2x2):
            return Matrix2x2(self.x11 + other.x11, self.x12 + other.x12, self.x21 + other.x21, self.x22 + other.x22)
        else:
            raise TypeError("Can only add Matrix2x2 objects")

    def __iadd__(self, other):
        if isinstance(other, Matrix2x2):
            self.x11 += other.x11
            self.x12 += other.x12
            self.x21 += other.x21
            self.x22 += other.x22
            return self
        else:
            raise TypeError("Can only add Matrix2x2 objects")

    def __sub__(self, other):
        if isinstance(other, Matrix2x2):
            return Matrix2x2(self.x11 - other.x11, self.x12 - other.x12, self.x21 - other.x21, self.x22 - other.x22)
        else:
            raise TypeError("Can only subtract Matrix2x2 objects")

    def __isub__(self, other):
        if isinstance(other, Matrix2x2):
            self.x11 -= other.x11
            self.x12 -= other.x12
            self.x21 -= other.x21
            self.x22 -= other.x22
            return self
        else:
            raise TypeError("Can only subtract Matrix2x2 objects")

    def __mul__(self, other):
        if isinstance(other, Matrix2x2):
            return Matrix2x2(
                self.x11 * other.x11 + self.x12 * other.x21,
                self.x11 * other.x12 + self.x12 * other.x22,
                self.x21 * other.x11 + self.x22 * other.x21,
                self.x21 * other.x12 + self.x22 * other.x22
            )
        elif isinstance(other, (int, float)):
            return Matrix2x2(self.x11 * other, self.x12 * other, self.x21 * other, self.x22 * other)
        else:
            raise TypeError("Can multiply only by Matrix2x2 or number")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Division by zero")
            return Matrix2x2(self.x11 / scalar, self.x12 / scalar, self.x21 / scalar, self.x22 / scalar)
        else:
            raise TypeError("Division only by int or float")

    def determinant(self):
        return self.x11 * self.x22 - self.x12 * self.x21

    def transpose(self):
        return Matrix2x2(self.x11, self.x21, self.x12, self.x22)

n = Matrix2x2(2355211, 197868, 12, 23453422)
print(n)
n1 = Matrix2x2(1523, -1253, 0, 1111)
n2 = n + n1
print(n2)
n2 -= n
print(n2)