from FunctionBase import FunctionBase
from FunctionExponent import FunctionExponent
from CalculationErrorException import CalculationErrorException

class FunctionSinh(FunctionBase):
    
    #constructor
    def __init__(self, num: float) -> None:
        super(FunctionSinh, self).__init__()
        self.num = num

    # calculate sinh
    # input: num (int), isDeg (boolean)
    # output: sinh(num)
    def calculateEquation(self, isDeg=False) -> float:

        #if the number is in degrees, convert it to radians
        if(isDeg):
            self.num = self.num * self.PI/180
            
        #calculate sinh using (e^x-e^-x)/2
        # https://www.whitman.edu/mathematics/calculus_online/section04.11.html
        num1 = FunctionExponent(self.e, self.num).calculateEquation()
        num2 = FunctionExponent(self.e, -self.num).calculateEquation()
        result = (num1-num2)/2
        
        #handle exceptions. We don't want a number too large or small
        if(result > self.MAX_RESULT):
            raise CalculationErrorException("result too large")
        elif(result < self.MIN_RESULT):
            raise CalculationErrorException("result too small")      
          
        return round(result,5)
