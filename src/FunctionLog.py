from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
from FunctionExponent import FunctionExponent
from FunctionAbs import FunctionAbs

# FunctionLog: Class used to evaluate logarithm
class FunctionLog(FunctionBase):

    # constructor: initialize the class, takes in b and b such that log_b(n)
    def __init__(self, b: float, n: float) -> None:
        super(FunctionLog, self).__init__()
        self.b = b #base
        self.n = n #value

    # defining ln through Taylor Series
    def ln(y: float) -> float:

        # x represents the exponent
        x = y - 1

        # i represents the starting integer for the riemann sum
        i = 1

        # creating sum var
        sum = 0

        # loop until the end condition is met
        for k in range(self.MAX_TERMS):

            # adding the values
            add = FunctionExponent(-1, k + 1).calculateEquation() * FunctionExponent(x, i).calculateEquation() / i

            # stop when the difference is smaller than 0.0000000001
            if FunctionAbs(add).calculateEquation() < 0.0000000001:
                break
            sum += add

            # move to the next integer in the riemann sum
            i += 1
        return sum

    # calculateEquation: Method that is called to calculate any exponents
    def calculateEquation(self) -> float:

        # validating both base and argument provided
        if self.n > 0 and self.b > 1:

            # using log identity: log_b(n) = log_x(n) / log_x(b)
            result = ln(self.n) / ln(self.b)

            # handle exceptions for results that are too large or small
            if(result > self.MAX_RESULT):
                raise CalculationErrorException("MATH ERROR: Result too large")
            elif(result < self.MIN_RESULT):
                raise CalculationErrorException("MATH ERROR: Result too small")

            return result
        else:
            raise CalculationErrorException("Invalid input, validate base and argument values.")
