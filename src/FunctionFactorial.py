from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException

class FunctionFactorial(FunctionBase):
    '''Class used to calculate the factorial function.'''

    def __init__(self, x: int) -> None:
        '''Constructor.'''
        super(FunctionFactorial, self).__init__()
        self.x = x

    def calculateEquation(self) -> int:
        '''Function used to calculate factorial'''

        if isinstance(self.x, float):
            raise CalculationErrorException('Invalid Input: Factorial input cannot be a decimal value.')

        # (-x)! is not valid
        if self.x < 0:
            raise CalculationErrorException('Invalid Input: Factorial input cannot be negative.')

        # 0! = 1
        elif self.x == 0:
            return 1

        # Calculate x!
        else:
            result = self.x
            i = result - 1
            while i > 0:
                result = result * i
                i = i - 1
            return result
