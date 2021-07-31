from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
import FunctionArcsin

class FunctionArccos(FunctionBase):
    '''Class used to calculate the arccos function.'''

    def __init__(self, num: float) -> None:
        '''Constructor.'''
        super(FunctionArccos, self).__init__()
        self.num = num
    
    def calculateEquation(self, isDeg=False) -> float:
        '''
            Function used to calculate arccos using arcsin.
            Returns arccos(self.num)
        '''

        # If the number is in degrees, convert it to radians
        if(isDeg):
            self.num = self.degreeToRadian(self.num)
   
        # To achieve Arccos(x) simply divide 2/pi - Arcsin(x)
        result = (self.PI/2) - FunctionArcsin.FunctionArcsin(self.num).calculateEquation()
        return result

if __name__ == '__main__':
    print(FunctionArccos(0.5).calculateEquation())