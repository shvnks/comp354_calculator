from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException

# Might rework and use for later
#from FunctionExponent import FunctionExponent
#from FunctionFactorial import FunctionFactorial

# FunctionLog: Class used to evaluate logarithm
class FunctionLog(FunctionBase):

    # constructor: initialize the class, takes in b and b such that log_b(n)
    def __init__(self, b: float, n: float) -> None:
        super(FunctionExponent, self).__init__()
        self.b = b #base
        self.n = n #value

    # common way to simplify computing log
    def binaryLog(n: float) -> float:
        if n == 0:
            CalculationErrorException("Invalid 'x' option, there is not log_2(0)")
        value = -1
        while(n):
            value += 1
            n >>= 1
        return value


    # calculateEquation: Method that is called to calculate any log
    def calculateEquation(b: float, n: float) -> float:
        # log_b(n) = log_x(n) / log_x(b)
        return binaryLog(n) / binaryLog(b)
