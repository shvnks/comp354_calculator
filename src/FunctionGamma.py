from FunctionBase import FunctionBase
from FunctionExponent import FunctionExponent
from FunctionSinh import FunctionSinh
from CalculationErrorException import CalculationErrorException

g = 7
lanczos_coef = [
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7]


class FunctionGamma(FunctionBase):

    # constructor
    def __init__(self, num: float) -> None:
        super(FunctionGamma, self).__init__()
        self.num = num

    def calculateEquation(self) -> float:
        if self.num < 0.5:
            return (self.PI / (FunctionSinh(self.PI * self.num).calculateEquation() * FunctionGamma(
                1 - self.num).calculateEquation())).real
            # return pi / (sin(pi*z)*gamma(1-z))
        else:
            self.num -= 1
            x = lanczos_coef[0]
            for i in range(1, g + 2):
                x += lanczos_coef[i] / (self.num + i)
            t = self.num + len(lanczos_coef) - 1.5

            return (sqrt(2 * self.PI) * FunctionExponent(t, self.num + 0.5).calculateEquation() * FunctionExponent(self.e,-t).calculateEquation() * x).real
            # return sqrt(2*pi) * t**(z+0.5) * exp(-t) * x


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.img = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result


# def absolute(self, number):
#     if number < 0:
#         return number * -1
#     else:
#         return number

def simple_abs(num):
    val = -num if num < 0 else num
    if val == -0.0:
        return 0.0
    else:
        return val


# def Square(n, i, j):
#     mid = (i + j) / 2
#     mul = mid * mid
#
#     # If mid itself is the square root,
#     # return mid
#     if (mul == n) or (simple_abs(mul - n) < 0.00001):
#         return mid
#
#     # If mul is less than n, recur second half
#     elif mul < n:
#         return Square(n, mid, j)
#
#     # Else recur first half
#     else:
#         return Square(n, i, mid)
#
#
# # Function to find the square root of n
# def findSqrt(num):
#     i = 1
#
#     # While the square root is not found
#     found = False
#     while found is False:
#
#         # If n is a perfect square
#         if i * i == num:
#             print(i)
#             found = True
#
#         elif i * i > num:
#
#             # Square root will lie in the
#             # interval i-1 and i
#             res = Square(num, i - 1, i)
#             print("{0:.5f}".format(res))
#             found = True
#         i += 1

def sqrt(N):
    if N < 0:
        print('Square root of negative number does not exist!')
        return
    else:
        # print(f'Square root of number {N}: {FunctionExponent(N, 1/2.0).calculateEquation()}')
        return FunctionExponent(N, 1 / 2.0).calculateEquation()

# Driver code
if __name__ == '__main__':
    print(FunctionGamma(2).calculateEquation())

