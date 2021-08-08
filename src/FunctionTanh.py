from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
import FunctionSinh
import FunctionCosh

class FunctionTanh(FunctionBase):
    '''Class used to calculate the Cosh function.'''
    
    def __init__(self, num: float) -> None:
        '''Constructor.'''
        super(FunctionTanh, self).__init__()
        self.num = num

    def calculateEquation(self, isDeg:bool = False) -> float:
        '''
            Function used to calculate cosh using exponents.
            Returns sinh(self.num)
        '''

        # If the number is in degrees, convert it to radians
        num = self.num
        if(isDeg):
            num = self.degreeToRadian(num)
            
        # Calculate tanh(x) using sinh(x)/cosh(x), where x is self.num
        # https://www.whitman.edu/mathematics/calculus_online/section04.11.html
        num1 = FunctionSinh.FunctionSinh(num).calculateEquation()
        num2 = FunctionCosh.FunctionCosh(num).calculateEquation()
        result = num1/num2
               
        return self.truncate(result, self.ROUNDING)
