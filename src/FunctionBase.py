
from abc import ABC, abstractmethod

class FunctionBase(ABC):
    '''Base class for all custom Math Functions'''

    def __init__(self) -> None:
        '''Constructor. Initialize constants'''
        super(ABC, self).__init__()
        self.MAX_TERMS = 170
        self.PI = 3.1415926535897932384626433
        self.e = 2.7182818284590452353602874
        self.MAX_RESULT = 10000000
        self.MIN_RESULT = -10000000
        self.ROUNDING = 9

    @abstractmethod
    def calculateEquation(self) -> float:
        '''Abstact function that will be used to calculate the math function'''
        raise NotImplementedError()

    def degreeToRadian(self, degreeValue):
        '''Function used to convert degrees to radians for trig functions'''
        return degreeValue * self.PI/180

    def truncate(self, value: float, decimal: int) -> float:
        '''Function used to reduce the number of decimal places'''
        return float(('%.' + str(decimal) + 'f') % (value))
