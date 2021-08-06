from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
from FunctionSinh import FunctionSinh
from FunctionCosh import FunctionCosh

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
        if(isDeg):
            self.num = self.degreeToRadian(self.num)
            
        # Calculate tanh(x) using sinh(x)/cosh(x), where x is self.num
        # https://www.whitman.edu/mathematics/calculus_online/section04.11.html
        num1 = FunctionSinh(self.num).calculateEquation()
        num2 = FunctionCosh(-self.num).calculateEquation()
        result = num1/num2
               
        return result