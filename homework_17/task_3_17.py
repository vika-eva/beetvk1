
class Fraction:

    def _reduce(self, n, d, sign):
        a = abs(n)
        b = abs(d)
        while a % b != 0:
            tempA = a
            tempB = b
            a = tempB
            b = tempA % tempB
        ret_n = abs(n) // b * sign
        ret_d = abs(d) // b * sign
        return ret_n, ret_d

    def getNumerator(self):
        return self._numerator

    def getDenominator(self):
        return self._denominator


    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('numerator and denominator must be integers')
        if denominator == 0:
            raise ZeroDivisionError('denominator cannot be zero')
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
                sign = -1
            else:
                sign = 1
            (self._numerator, self._denominator) = self._reduce(numerator, denominator, sign)

    def __repr__(self):
        return str(self._numerator) + '/' + str(self._denominator)

    def __eq__(self, rhs):
        lhs = self
        return (lhs.getNumerator() == rhs.getNumerator()) and (lhs.getDenominator() == rhs.getDenominator())

    def __ne__(self, rhs):
        lhs = self
        return not lhs == rhs

    def __lt__(self, rhs):
        lhs = self
        return lhs.getNumerator()* rhs.getDenominator() < lhs.getDenominator() * rhs.getNumerator()

    def __le__(self, rhs):
        lhs = self
        return not rhs < lhs # not rhs < lhs

    def __gt__(self, rhs):
        lhs = self
        return lhs > rhs

    def __ge__(self, rhs):
        lhs = self
        return not rhs > lhs

    def __add__(self, rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenominator() + rhs.getNumerator() * lhs.getDenominator()
        den = lhs.getDenominator() * rhs.getDenominator()
        return Fraction(num, den)

    def __sub__(self, rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenominator() - rhs.getNumerator() * lhs.getDenominator()
        den = lhs.getDenominator() * rhs.getDenominator()
        return Fraction(num, den)

    def __truediv__(self, rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenominator()
        den = lhs.getDenominator() * rhs.getNumerator()
        return Fraction(num, den)


x = Fraction(1, 2)
y = Fraction(1, 4)
print(Fraction.__add__(x, y))




