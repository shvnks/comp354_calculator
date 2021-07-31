from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
from FunctionExponent import FunctionExponent
from FunctionAbs import FunctionAbs

class FunctionLog(FunctionBase):
    '''Class used to calculate the log function.'''

    def __init__(self, b: float, n: float) -> None:
        '''Constructor, where b is the base and n is the value'''
        super(FunctionLog, self).__init__()
        self.b = b
        self.n = n

    def ln(y: float) -> float:
        '''Function used to calculate ln through Taylor Series'''

        # x represents the exponent
        x = y - 1

        # i represents the starting integer for the riemann sum
        i = 1

        # Creating the sum variable
        sum = 0

        # Loop until the end condition is met
        for k in range(self.MAX_TERMS):

            # Adding the values
            add = FunctionExponent(-1, k + 1).calculateEquation() * FunctionExponent(x, i).calculateEquation() / i

            # Stop when the difference is smaller than 0.0000000001
            if FunctionAbs(add).calculateEquation() < 0.0000000001:
                break
            sum += add

            # Move to the next integer in the riemann sum
            i += 1
        return sum

    def calculateEquation(self) -> float:
        '''
            Function used to calculate log.
            Returns log with base self.b of self.n
        '''

        # Validating both base and argument provided
        if self.n > 0 and self.b > 1:

            # Using log identity: log_b(n) = log_x(n) / log_x(b)
            result = ln(self.n) / ln(self.b)

            # Handle exceptions for results that are too large or small
            if(result > self.MAX_RESULT):
                raise CalculationErrorException("MATH ERROR: Result too large")
            elif(result < self.MIN_RESULT):
                raise CalculationErrorException("MATH ERROR: Result too small")

            return result
        else:
            raise CalculationErrorException("Invalid Input: validate base and argument values.")
