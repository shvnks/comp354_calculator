from typing import List

from FunctionExponent import FunctionExponent

class FunctionStandardDeviation():
    '''Class used to calculate StandardDeviation.'''

    def __init__(self, values : List[float]):
        '''Constructor. Takes in array of values.'''
        self.values = values

    def getMean(self):
        '''Calculate average.'''
        self.mean = 0
        for point in self.values:
            self.mean += point
        self.mean /= len(self.values)

    def standard_deviation(self):
        '''Calculate standard deviation.'''
        # Gets average of data points in self.values
        self.getMean()
        standard_deviation = 0

        # Calculation of Σ(point - mean)^2
        for point in self.values:
            standard_deviation += FunctionExponent((point - self.mean), 2).calculateEquation()

        # Returns sqrt(Σ(point - mean)^2 / Number of points)
        return FunctionExponent((standard_deviation / len(self.values)), 0.5).calculateEquation()
