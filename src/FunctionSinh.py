from FunctionBase import FunctionBase
from FunctionFactorial import FunctionFactorial
from FunctionExponent import FunctionExponent

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
            
        #calculate sinh
        num1 = self.__custom_exp(self.num)
        num2 = self.__custom_exp(-self.num)
        result = (num1-num2)/2
        
        #handle exceptions. We don't want a number too large or small
        if(result > self.MAX_RESULT):
            raise Exception("result too large")
        elif(result < self.MIN_RESULT):
            raise Exception("result too small")      
          
        return round(result,5)


    # calculate e^x (private helper function) using Mclaurin Series
    # input: x (int)
    # output: e^x
    def __custom_exp(self,x):
        n=0
        for i in range(0, self.MAX_TERMS):
            n= n + (FunctionExponent(x,i).calculateEquation())/(FunctionFactorial(i).calculateEquation())
        return n