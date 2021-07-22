from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
from FunctionArcsin import FunctionArcsin
import math


# FunctionArcsin: Class use to define and calculate Arcsin(x)
class FunctionAcrcos(Functionbase):

        def my_arccos(x):
            # To achieve Arccos(x) simply divide 2/pi - Arcsin(x)
            my_pi = 3.141592653589793238
            arccos = ((my_pi/2) - FunctionArcsin(FunctionBase))
            return arccos