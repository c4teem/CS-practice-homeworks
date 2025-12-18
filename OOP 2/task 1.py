class RationalFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            raise ZeroDivisionError("You cannot divide by zero!!!")


    def __gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x


    def __reduction(self, x, y):
        d = self.__gcd(x, y)
        x //= d
        y //= d
        return x, y
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


    def reduce(self):
        d = self.__reduction(self.numerator, self.denominator)
        self.numerator = d[0]
        self.denominator = d[1]


    def __add__(self, fraction):
        new_numerator = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        new_denominator = self.denominator * fraction.denominator

        new_numerator, new_denominator = self.__reduction(new_numerator, new_denominator)
        return RationalFraction(new_numerator, new_denominator)


    def __iadd__(self, fraction):
        self.numerator = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        self.denominator = self.denominator * fraction.denominator
        
        self.numerator, self.denominator = self.__reduction(self.numerator, self.denominator)
        return self


    def __sub__(self, fraction):
        new_numerator = self.numerator * fraction.denominator - fraction.numerator * self.denominator
        new_denominator = self.denominator * fraction.denominator

        new_numerator, new_denominator = self.__reduction(new_numerator, new_denominator)
        return RationalFraction(new_numerator, new_denominator)
    

    def __isub__(self, fraction):
        self.numerator = self.numerator * fraction.denominator - fraction.numerator * self.denominator
        self.denominator = self.denominator * fraction.denominator
        
        self.numerator, self.denominator = self.__reduction(self.numerator, self.denominator)
        return self


    def __mul__(self, fraction):
        new_numerator = self.numerator * fraction.numerator
        new_denominator = self.denominator * fraction.denominator

        new_numerator, new_denominator = self.__reduction(new_numerator, new_denominator)
        return RationalFraction(new_numerator, new_denominator)

    def __imul__(self, fraction):
       self.numerator = self.numerator * fraction.numerator
       self.denominator = self.denominator * fraction.denominator
       
       self.numerator, self.denominator = self.__reduction(self.numerator, self.denominator)
       return self

    def __truediv__(self, fraction):
        new_numerator = self.numerator * fraction.denominator
        new_denominator = self.denominator * fraction.numerator

        new_numerator, new_denominator = self.__reduction(new_numerator, new_denominator)
        return RationalFraction(new_numerator, new_denominator)


    def __itruediv__(self, fraction):
       self.numerator = self.numerator * fraction.denominator
       self.denominator = self.denominator * fraction.numerator
       
       self.numerator, self.denominator = self.__reduction(self.numerator, self.denominator)
       return self


    def to_float(self):
        return self.numerator / self.denominator

    def __eq__(self, fraction):
        return self.numerator * fraction.denominator == self.denominator * fraction.numerator
    

ex1 = RationalFraction(23, 11)
ex2 = RationalFraction(3, 34)
ex3 = RationalFraction(3, 11)
ex4 = RationalFraction(11, 22)
ex5 = RationalFraction(23, 23351)
ex6 = RationalFraction(46, 22)

print("\n")
print(ex4)
print(ex5)

print("\n")
n = ex1 + ex2
print(n)

print("\n")
print(ex1)
ex1 += ex2
print(ex1)

print("\n")
print(ex1)
ex1 -= ex2
print(ex1)

print("\n")
print(ex1.to_float())

print("\n")
print(ex1 == ex6)
