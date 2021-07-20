
from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException

# FunctionFactorial: Class used to evaluate factorials
class FunctionFactorial(FunctionBase):

    # constructor: initialize the class, takes in x such that x!
    def __init__(self, x: int) -> None:
        super(FunctionFactorial, self).__init__()
        self.x = x

    # calculateEquation: Method that is called to calculate any factorials
    def calculateEquation(self) -> int:

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
