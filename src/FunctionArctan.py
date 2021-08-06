from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
import FunctionArcsin
import FunctionExponent

class FunctionArctan(FunctionBase):
    '''Class used to calculate the arctan function.'''

    def __init__(self, num: float) -> None:
        '''Constructor.'''
        super(FunctionArctan, self).__init__()
        self.num = num
    
    def calculateEquation(self, isDeg=False) -> float:
        '''
            Function used to calculate arccos using arcsin.
            Returns arccos(self.num)
        '''

        # If the number is in degrees, convert it to radians
        num = self.num
        if(isDeg):
            num = self.degreeToRadian(num)
   
        # To achieve Arctan(x) use arcsin: arctan(x) = arcsin(x/(sqrt(1+x^2)))
        # Source: https://en.wikipedia.org/wiki/Inverse_trigonometric_functions
        result = FunctionArcsin.FunctionArcsin( num / FunctionExponent.FunctionExponent(1+(num * num), 0.5).calculateEquation()).calculateEquation()
        return result

if __name__ == '__main__':
    print(FunctionArctan(0.5).calculateEquation())