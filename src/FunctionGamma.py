from FunctionBase import FunctionBase
from FunctionExponent import FunctionExponent
from FunctionSinh import FunctionSinh
from CalculationErrorException import CalculationErrorException

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

    # Gamma Function
    # Input: Value to calculate
    # Output: Result from gamma function
    def calculateEquation(self) -> float:
        if self.num < 0.5:
            return (self.PI / (FunctionSinh(self.PI * self.num).calculateEquation() * FunctionGamma(1 - self.num).calculateEquation()))
            # return pi / (sin(pi*self.num)*gamma(1-z))
        else:
            self.num -= 1
            x = lanczos_coef[0]
            for i in range(1, 9):
                x += lanczos_coef[i] / (self.num + i)
            t = self.num + len(lanczos_coef) - 1.5

            return (sqrt(2 * self.PI) * FunctionExponent(t, self.num + 0.5).calculateEquation() * FunctionExponent(self.e, -t).calculateEquation() * x)
            # return sqrt(2*pi) * t**(self.num+0.5) * exp(-t) * x

# A simple square root function
def sqrt(N):
    if N < 0:
        print('Square root of negative number does not exist!')
        return
    else:
        # print(f'Square root of number {N}: {FunctionExponent(N, 1/2.0).calculateEquation()}')
        return FunctionExponent(N, 1 / 2.0).calculateEquation()


# Driver code
if __name__ == '__main__':
    print(FunctionGamma(1).calculateEquation())
