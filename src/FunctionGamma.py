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
    '''Class used to calculate the Gamma function.'''

    def __init__(self, num: float) -> None:
        '''Constructor.'''
        super(FunctionGamma, self).__init__()
        self.num = num

    def calculateEquation(self) -> float:
        '''
            Function used to calculate the gamma function.
            Returns Gamma(self.num)
        '''
        if self.num < 0.5:
            return (self.PI / (FunctionSinh(self.PI * self.num).calculateEquation() * FunctionGamma(1 - self.num).calculateEquation()))
        else:
            self.num -= 1
            x = lanczos_coef[0]

            for i in range(1, 9):
                x += lanczos_coef[i] / (self.num + i)

            t = self.num + len(lanczos_coef) - 1.5

            return (FunctionExponent(2 * self.PI, 0.5).calculateEquation() * FunctionExponent(t, self.num + 0.5).calculateEquation() * FunctionExponent(self.e, -t).calculateEquation() * x)


# Test Code
if __name__ == '__main__':
    print(FunctionGamma(1).calculateEquation())
