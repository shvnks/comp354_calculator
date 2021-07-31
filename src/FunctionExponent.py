
from CalculationErrorException import CalculationErrorException
from FunctionBase import FunctionBase
from FunctionFactorial import FunctionFactorial
from FunctionLog import FunctionLog

class FunctionExponent(FunctionBase):
    '''Class used to calculate the Exponent function.'''

    def __init__(self, x: float, y: float) -> None:
        super(FunctionExponent, self).__init__()
        self.x = x
        self.y = y

    def __calculateIntExponent(self, x: int, y: int) -> float:
        '''
            Function used to calculate the exponents  using x and y, 
            such that x^y, and x and y are integers.
            Returns x^y
        '''

        # x^0 = 1
        if y == 0:
            return 1

        # 0^x = 0
        elif x == 0:
            return 0

        # x^y where y is an integer
        else:
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

    def calculateEquation(self) -> float:
        '''
            Function used to calculate any x^y.
            Returns x^y
        '''

        if self.x == 0 and self.y < 0:
            raise CalculationErrorException('Invalid Input: Base of 0 cannot be raise to a negative value')

        if self.x < 0 and self.y < 0 and not isinstance(self.y, int):
            raise CalculationErrorException('Invalid Input: Negative Base exponent cannot be raised to negative decimals')

        # Don't need to do the Taylor Expansion of it meets any of those requirements
        if self.y == 0 or self.x == 0 or isinstance(self.y, int):
            return self.__calculateIntExponent(x = self.x, y = self.y)
        else:

            # Any exponent can be calculated this way: a^b = e^(b*ln(a))
            # and then the e^x can be approximated using the Taylor Series Expension:
            # e^x = Sum_{i=1}^{\inft}( x^{i-1} ) \ ( (i-1)! )

            # https://math.stackexchange.com/a/21386/766151
            # https://math.stackexchange.com/questions/1124242/how-to-calculate-exp-x-using-taylor-series

            selfxabs = self.x

            x = self.y * FunctionLog(self.e, self.x).calculateEquation()
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