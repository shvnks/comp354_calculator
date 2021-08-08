from typing import List

from FunctionBase import FunctionBase
import FunctionExponent

class FunctionStandardDeviation(FunctionBase):
    '''Class used to calculate StandardDeviation.'''

    def __init__(self, values : List[float]):
        '''Constructor. Takes in array of values.'''
        super(FunctionStandardDeviation, self).__init__()
        self.values = values

    def getMean(self):
        '''Calculate average.'''
        mean = 0
        for point in self.values:
            mean += point
        mean /= len(self.values)
        return mean

    def calculateEquation(self):
        '''Calculate standard deviation.'''
        # Gets average of data points in self.values

        mean = self.getMean()
        standard_deviation = 0

        # Calculation of Σ{(point - mean)^2}
        for point in self.values:
            standard_deviation += FunctionExponent.FunctionExponent((point - mean), 2).calculateEquation()

        # Returns sqrt(Σ(point - mean)^2 / Number of points)
        return round(FunctionExponent.FunctionExponent((standard_deviation / len(self.values)), 0.5).calculateEquation(), self.ROUNDING)
