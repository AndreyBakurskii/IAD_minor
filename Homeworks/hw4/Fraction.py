class Fraction():
    def __init__(self, num: int, den: int):

        nod = self._nod(abs(num), den)

        self.num = num // nod
        self.den = den // nod

    def __add__(self, other):

        nok = self._nok(self.den, other.den)

        num = self.num * (nok // self.den) + other.num * (nok // other.den)
        den = nok

        return Fraction(num, den)

    def __sub__(self, other):
        nok = self._nok(self.den, other.den)

        num = self.num * (nok // self.den) - other.num * (nok // other.den)
        den = nok

        return Fraction(num, den)

    def __mul__(self, other):

        num = self.num * other.num
        den = self.den * other.den

        return Fraction(num, den)

    def __truediv__(self, other):

        num = self.num * other.den
        den = self.den * other.num

        return Fraction(num, den)

    def __lt__(self, other):  # <
        if (self - other).num < 0:
            return True
        return False

    def __le__(self, other):  # <=
        if (self - other).num <= 0:
            return True
        return False

    def __eq__(self, other):  # ==
        if (self - other).num == 0:
            return True
        return False

    def __ne__(self, other):  # !=
        if (self - other).num != 0:
            return True
        return False

    def __gt__(self, other):  # >
        if (self - other).num > 0:
            return True
        return False

    def __ge__(self, other):  # >=
        if (self - other).num >= 0:
            return True
        return False

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __str__(self):
        return f"{self.num}/{self.den}"

    def _nod(self, a: int, b: int):

        if a == 0 or b == 0:
            return max(a, b)

        return self._nod(b % a, a)

    def _nok(self, a: int, b: int):
        return (a * b) // self._nod(a, b)


fraction = Fraction(26, 4)

print(fraction)
