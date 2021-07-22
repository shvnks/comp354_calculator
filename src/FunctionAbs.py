
from CalculationErrorException import CalculationErrorException
from FunctionBase import FunctionBase

import math

# FunctionExponent: Class used to evaluate exponents
class FunctionAbs(FunctionBase):

    # constructor: initialize the class, takes in x and y such that x^y
    def __init__(self, x: float) -> None:
        super(FunctionAbs, self).__init__()
        self.x = x

    # calculateEquation: Method that is called to calculate any exponents
    def calculateEquation(self) -> float:
        result = self.x
        if result < 0:
            result = -1 * result
        
        if result > self.MAX_RESULT:
            raise CalculationErrorException('Result too high')
        if result < self.MIN_RESULT:
            raise CalculationErrorException('Result too low')

        return result