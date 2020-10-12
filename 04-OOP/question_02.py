class Rational:
    # gcd recursive
    def __gcd(self, a, b):
        if(b == 0):
            return a
        else:
            return self.__gcd(b, a % b)

    # constructor / instance attributes
    def __init__(self, n=0, d=1):
        if d == 0:
            raise SystemExit("denom must not be zero!")

        self.__g = self.__gcd(n, d)
        self.numer = n//self.__g
        self.denom = d//self.__g

    # override add operator (rational)
    def __add__(self, other):
        if isinstance(other, int):
            return self + Rational(other)
        else:
            # common = self.__gcd(self.numer, self.denom)
            new_numer = self.numer*other.denom + other.numer*self.denom
            new_denom = self.denom*other.denom
            return Rational(new_numer, new_denom)

    # override string convert method
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)


print(Rational(1, 2) + 2)
print(Rational(1,2) + Rational(1,2))
print(Rational())
