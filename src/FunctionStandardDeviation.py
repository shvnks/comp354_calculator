"""Calculating Standard Deviation."""
from FunctionExponent import FunctionExponent


class FunctionStandardDeviation():
    """Calculate StandardDeviation."""

    def __init__(self, values):
        """Initialize class with an array of values."""
        self.values = values

    def getMean(self):
        """Acquire Average."""
        self.mean = 0
        for point in self.values:
            self.mean += point
        self.mean /= len(self.values)

    def standardDeviation(self):
        """Calculate standard deviation."""
        self.getMean()  # Gets average of data points in self.values
        standard_deviation = 0

        for point in self.values:  # Calculation of Σ(point - mean)^2
            standard_deviation += FunctionExponent((point - self.mean), 2).calculateEquation()

        # Returns sqrt(Σ(point - mean)^2 / Number of points)
        return FunctionExponent((standard_deviation / len(self.values)), 0.5).calculateEquation()
