
from CalculationErrorException import CalculationErrorException
from FunctionBase import FunctionBase
import FunctionFactorial
import FunctionLog

class FunctionExponent(FunctionBase):
    '''Class used to calculate the Exponent function.'''

    def __init__(self, x: float, y: float) -> None:
        super(FunctionExponent, self).__init__()
        self.x = x
        self.y = y

    def __calculateIntExponent(self, x: float, y: int) -> float:
        '''
            Function used to calculate the exponents  using x and y, 
            such that x^y, and x and y are integers.
            Returns x^y
        '''

        # x^0 = 1
        if y == 0:
            return 1

        # 0^x = 0
        if x == 0:
            return 0

        # x^y where y is an integer
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
            raise CalculationErrorException('Invalid Input: Base of 0 cannot be raised to a negative value')

        if self.x < 0 and self.y < 0 and int(self.y) != self.y:
            raise CalculationErrorException('Invalid Input: Negative base exponent cannot be raised to negative decimals')

        # Don't need to do the Taylor Expansion of it meets any of those requirements
        if self.y == 0 or self.x == 0 or int(self.y) == self.y:
            return self.__calculateIntExponent(x = self.x, y = int(self.y))
        else:

            # Any exponent can be calculated this way: a^b = e^(b*ln(a))
            # and then the e^x can be approximated using the Taylor Series Expension:
            # e^x = Sum_{i=1}^{\inft}( x^{i-1} ) \ ( (i-1)! )

            # https://math.stackexchange.com/a/21386/766151
            # https://math.stackexchange.com/questions/1124242/how-to-calculate-exp-x-using-taylor-series

            a = self.y * FunctionLog.FunctionLog(self.e, self.x).calculateEquation()
            aabs = a
            if aabs < 0:
                aabs = aabs * -1

            # Taylor series
            sum = 0
            for i in range(1, self.MAX_TERMS):
                sum = sum + ((self.__calculateIntExponent(x = aabs, y = (i - 1)))/(FunctionFactorial.FunctionFactorial(i - 1).calculateEquation()))

            # Invert it if the exponent was negative
            if a < 0:
                sum = 1 / sum

            return self.truncate(sum, self.ROUNDING)


if __name__ == '__main__':
    print(FunctionExponent(0.5, 100).calculateEquation())