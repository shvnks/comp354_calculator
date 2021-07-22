from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
from FunctionExponent import FunctionExponent

# FunctionLog: Class used to evaluate logarithm
class FunctionLog(FunctionBase):

    # constructor: initialize the class, takes in b and b such that log_b(n)
    def __init__(self, b: float, n: float) -> None:
        super(FunctionExponent, self).__init__()
        self.b = b #base
        self.n = n #value

    # defining ln through Taylor Series
    def ln(y: float) -> float:

        # x represents the exponent
        x = y - 1

        # k represents the starting integer for the riemann sum
        k = 1

        # creating sum var
        sum = 0

        # loop until the end condition is met
        while True:

            # adding the values
            add = FunctionExponent(-1).calculateEquation(k + 1) * FunctionExponent(x).calculateEquation(i) / i

            # stop when the difference is smaller than 0.0000000001
            if abs(add) < 0.0000000001:
                break
            sum += add

            # move to the next integer in the riemann sum
            i += 1
        return sum

    # # calculateEquation: Method that is called to calculate any exponents
    def calculateEquation(self) -> float:

        # validating both base and argument provided
        if self.x > 0 and self.b > 1:

            # using log identity: log_b(n) = log_x(n) / log_x(b)
            result = ln(self.n) / ln(self.b)

            # handle exceptions for results that are too large or small
            if(result > self.MAX_RESULT):
                raise CalculationErrorException("result too large")
            elif(result < self.MIN_RESULT):
                raise CalculationErrorException("result too small")

            return round(result,5)
        else:
            raise CalculationErrorException("Invalid input, check if the base is positive and greater than 1 as well as if the argument provided is positive.")
