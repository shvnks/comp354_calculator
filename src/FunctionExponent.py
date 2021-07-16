
from FunctionBase import FunctionBase
from FunctionFactorial import FunctionFactorial

import math

# FunctionExponent: Class used to evaluate exponents
class FunctionExponent(FunctionBase):

    # constructor: initialize the class, takes in x and y such that x^y
    def __init__(self, x: float, y: float) -> None:
        super(FunctionExponent, self).__init__()
        self.x = x
        self.y = y

    # calculateIntExponent: Private function used to calculate integer exponents
    def __calculateIntExponent(self, x: int, y: int) -> float:

        # x^0 = 1
        if y == 0:
            return 1
        
        # 0^x = 0
        elif x == 0:
            return 0
        
        # x^y where y is an integer
        elif isinstance(y, int):
            result = x
            yabs = y
            if yabs < 0:
                yabs = yabs * -1

            for i in range(1, yabs):
                result = result * x
            
            # if y was negative, then invert it, since x^(-y) = 1/(x^y)
            if y < 0:
                result = 1 / result
            return result

    # calculateEquation: Method that is called to calculate any exponents
    def calculateEquation(self) -> float:

        # Don't need to do the Taylor Expansion of it meets any of those requirements
        if self.y == 0 or self.x == 0 or isinstance(self.y, int):
            return self.evaluateIntExponent(x = self.x, y = self.y)
        else:

            #TODO: Replace ln from python with the manual implementation
            
            #Any exponent can be calculated this way: a^b = e^(b*ln(a))
            # and then the e^x can be approximated using the Taylor Series Expension: 
            # e^x = Sum_{i=1}^{\inft}( x^{i-1} ) \ ( (i-1)! )

            # https://math.stackexchange.com/a/21386/766151
            # https://math.stackexchange.com/questions/1124242/how-to-calculate-exp-x-using-taylor-series

            x = self.y * math.log(self.x)
            xabs = x
            if xabs < 0:
                xabs = xabs * -1

            # Taylor series
            sum = 0
            for i in range(1, self.MAX_TERMS):
                sum = sum + ((self.__calculateIntExponent(x = xabs, y = (i - 1)))/(FunctionFactorial(i - 1).calculateEquation()))

            # Invert it if the exponent was negative
            if x < 0:
                sum = 1 / sum

            return sum



        