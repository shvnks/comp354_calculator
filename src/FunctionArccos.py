from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
from FunctionArcsin import FunctionArcsin
import math


# FunctionArccos: Class use to define and calculate Arccos(x)
class FunctionArccos(FunctionBase):

     #constructor
    def __init__(self, num: float) -> None:
        super(FunctionArccos, self).__init__()
        self.num = num
    
    # Calculate Arccos(x)
    # Input: num (int), isDeg (boolean)
    # Output: Arccos(num)
    def calculateEquation(self, isDeg=False) -> float:

        # If the number is in degrees, convert it to radians
        if(isDeg):
            self.num = self.num * self.PI/180
   
        # To achieve Arccos(x) simply divide 2/pi - Arcsin(x)
        my_pi = 3.141592653589793238
        arccos = ((my_pi/2) - FunctionArcsin(FunctionBase).calculateEquation())
        return arccos