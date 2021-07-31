
from CalculationErrorException import CalculationErrorException
from FunctionBase import FunctionBase

class FunctionAbs(FunctionBase):
    '''Class used to calculate the Absolute function.'''

    def __init__(self, x: float) -> None:
        '''Constructor.'''
        super(FunctionAbs, self).__init__()
        self.x = x

    def calculateEquation(self) -> float:
        '''
            Function used to calculate the absolute value.
            Returns |self.x|
        '''
        result = self.x
        if result < 0:
            result = -1 * result
        
        if result > self.MAX_RESULT:
            raise CalculationErrorException('MATH ERROR: Result too high')
        if result < self.MIN_RESULT:
            raise CalculationErrorException('MATH ERROR: Result too low')

        return result