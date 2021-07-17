from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
from FunctionSinh import FunctionSinh
from FunctionCosh import FunctionCosh

class FunctionTanh(FunctionBase):
    
    #constructor
    def __init__(self, num: float) -> None:
        super(FunctionTanh, self).__init__()
        self.num = num

    # calculate sinh
    # input: num (int), isDeg (boolean)
    # output: sinh(num)
    def calculateEquation(self, isDeg=False) -> float:

        #if the number is in degrees, convert it to radians
        if(isDeg):
            self.num = self.num * self.PI/180
            
        #calculate tanh using sinh(x)/cosh(x)
        # https://www.whitman.edu/mathematics/calculus_online/section04.11.html
        num1 = FunctionSinh(self.num).calculateEquation()
        num2 = FunctionCosh(-self.num).calculateEquation()
        result = num1/num2
               
        return round(result,5)