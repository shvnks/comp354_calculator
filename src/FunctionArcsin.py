from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
import FunctionExponent
import FunctionFactorial

class FunctionArcsin(FunctionBase):
    '''Class used to calculate the arcsin function.'''    
    
    def __init__(self, num: float) -> None:
        '''Constructor.'''
        super(FunctionArcsin, self).__init__()
        self.num = num

    def __exp(self, x: float, y: float) -> float:
        return FunctionExponent.FunctionExponent(x, y).calculateEquation()

    def __fac(self, x: int) -> int:
        return FunctionFactorial.FunctionFactorial(x).calculateEquation()

    def calculateEquation(self, isDeg=False) -> float:
        '''
            Function used to calculate arccos using Taylor Series.
            Returns arcsin(self.num)
        '''

        # If the number is in degrees, convert it to radians
        num = self.num
        if(isDeg):
            num = self.degreeToRadian(num)
    
        sum = 0

	    # Taylor Series calculation.
        for n in range(0, self.MAX_TERMS):

            a1 = 1 / self.__exp(2, 2*n)

            a2 = self.__fac(2 * n) / (self.__fac(n) * self.__fac(n))

            a3 = self.__exp(num, (2 * n) + 1) / ((2 * n) + 1)

            sum = sum + (a1 * a2 * a3)

        return self.truncate(sum, self.ROUNDING-3)

if __name__ == '__main__':
    print(FunctionArcsin(0.5).calculateEquation())