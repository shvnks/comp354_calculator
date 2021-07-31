from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException

class FunctionArcsin(FunctionBase):
    '''Class used to calculate the arcsin function.'''    
    
    def __init__(self, num: float) -> None:
        '''Constructor.'''
        super(FunctionArcsin, self).__init__()
        self.num = num

    def calculateEquation(self, isDeg=False) -> float:
        '''
            Function used to calculate arccos using Taylor Series.
            Returns arcsin(self.num)
        '''

        # If the number is in degrees, convert it to radians
        if(isDeg):
            self.num = self.degreeToRadian(self.num)
    
        sum = 0

	    # Taylor Series calculation.
        for n in range(0, self.MAX_TERMS):

            # Formula of the Talor series in terms of the integration for arcsin
            x1 = (  self.num ** (2 * n + 1)) / (2 * n + 1) / float(2 ** (2 * n))
            x2 = float(1)        
        
            #top numerator of the integration 
            for i in range(n + 1, 2 * n + 1):
                x2 *= i

            #Divided by the bottom denominator of the intergration. 
            for i in range(2, n + 1):
                x2 /= i

	        #The addition to the next series with the multiplication of the intergration.
            sum += x1 * x2

        return sum

if __name__ == '__main__':
    print(FunctionArcsin(0.5).calculateEquation())