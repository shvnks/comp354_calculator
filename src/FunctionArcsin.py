

from FunctionBase import FunctionBase
from CalculationErrorException import CalculationErrorException
import math

# FunctionArcsin: Class use to define and calculate Arcsin(x)
class FunctionAcrsin(Functionbase):
    def my_arcsin(x):
        var_x = float(x)
        
            # sum1 variable is the sum of the series.
        sum1 = 0

	    # Current for loop to create the length of the series.
	    # Note that the range is set to 130 since anything greater can cause an overflow for different IDEs. 
        for n in range(0, 130):

        # Formula of the Talor series in terms of the integration for arcsin
            x1 = (var_x ** (2 * n + 1)) / (2 * n + 1) / float(2 ** (2 * n))
            x2 = float(1)        
        
        
            #top numerator of the integration 
            for i in range(n + 1, 2 * n + 1):
                x2 *= i
            #Divided by the bottom denominator of the intergration. 
            for i in range(2, n + 1):
                x2 /= i

	    #The addition to the next series with the multiplication of the intergration.
            sum1 += x1 * x2

        return sum1