from FunctionBase import FunctionBase
import FunctionExponent
from CalculationErrorException import CalculationErrorException

import math

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
        self.EPSILON = 1e-07
        
    def calculateEquation(self) -> float:
        '''
            Function used to calculate the gamma function.
            Returns Gamma(self.num)
        '''
        num = self.num
        if num < 0.5:
            return (self.PI / (math.sin(self.PI * num) * FunctionGamma(1 - num).calculateEquation()))
        else:
            num -= 1
            x = lanczos_coef[0]
            for i in range(1, len(lanczos_coef)):
                x += lanczos_coef[i] / (num + i)
            t = num + len(lanczos_coef) - 1.5
            y = FunctionExponent.FunctionExponent(2 * self.PI, 0.5).calculateEquation() * \
                    FunctionExponent.FunctionExponent(t, (num + 0.5)).calculateEquation() * \
                    FunctionExponent.FunctionExponent(self.e, -t).calculateEquation() * x
            return self.truncate(y, self.ROUNDING)


# Test Code
if __name__ == '__main__':
    print(FunctionGamma(1).calculateEquation())
