from FunctionBase import FunctionBase


class FunctionSinh(FunctionBase):
    
    #constants
    MAX_RESULT = 10000000
    MIN_RESULT = -10000000

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

    # calculate factorial (private helper function)
    # input: n (int)
    # output: n!
    def __custom_factorial(self,n:int):
        result=1
        if n==0:
            return 1
        
        elif n>0:
            for i in range(1,n+1):
                result = result*i
        return result


    # calculate e^x (private helper function) using Mclaurin Series
    # input: x (int)
    # output: e^x
    def __custom_exp(self,x):
        n=0
        for i in range(0, self.MAX_TERMS):
            n= n + (x**i)/(self.__custom_factorial(i))
        return n


