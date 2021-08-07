from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
import FunctionExponent
import FunctionAbs

class FunctionLog(FunctionBase):
    '''Class used to calculate the log function.'''

    def __init__(self, b: float, n: float) -> None:
        '''Constructor, where b is the base and n is the value'''
        super(FunctionLog, self).__init__()
        self.b = b
        self.n = n

    def ln(self, x: float) -> float:
        '''
            Function used to calculate ln through Series Expansion.
            Where ln(x) = 2 * Sum_1^\infty{ (((x-1)/(x+1))^(2n-1)) / (2n-1) }
            See: https://math.stackexchange.com/questions/977586/is-there-an-approximation-to-the-natural-log-function-at-large-values
        '''

        # Creating the sum variable
        sum = 0

        # Loop until the end condition is met
        for n in range(1, self.MAX_TERMS):
            y = (x-1)/(x+1)
            add = FunctionExponent.FunctionExponent(y, (2*n-1)).calculateEquation() / (2*n-1)
            sum += add

        return 2 * sum

    def calculateEquation(self) -> float:
        '''
            Function used to calculate log.
            Returns log with base self.b of self.n
        '''

        # Validating both base and argument provided
        if self.n > 0 and self.b > 1:

            # Using log identity: log_b(n) = log_x(n) / log_x(b)
            result = self.ln(self.n) / self.ln(self.b)

            # Handle exceptions for results that are too large or small
            if(result > self.MAX_RESULT):
                raise CalculationErrorException("MATH ERROR: Result too large")
            elif(result < self.MIN_RESULT):
                raise CalculationErrorException("MATH ERROR: Result too small")

            return result
        else:
            raise CalculationErrorException("Invalid Input: validate base and argument values.")


if __name__ == '__main__':
    print(FunctionLog(3, 4.7).calculateEquation())